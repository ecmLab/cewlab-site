#!/usr/bin/env python3
"""Refresh _data/scholar.yml from Google Scholar and the local bibliography.

Run monthly by .github/workflows/update-scholar.yml, or by hand:

    python3 bin/update_scholar.py

Design note: Google Scholar rate-limits datacenter IPs and serves a CAPTCHA
instead of the profile often enough that a scheduled job WILL sometimes fail.
This script treats that as normal — on any failure it leaves the existing file
untouched and exits 0, so the site keeps rendering the last known-good numbers
and the `updated` date shows how stale they are. It never writes zeros or
partial data, because a stat band reading "0 citations" is worse than one
reading numbers from last month.

The publication count is derived from _bibliography/papers.bib, so it is always
exact and never depends on the network.
"""

from __future__ import annotations

import datetime as dt
import pathlib
import re
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "_data" / "scholar.yml"
BIB = ROOT / "_bibliography" / "papers.bib"

PROFILE = "https://scholar.google.com/citations?user={uid}&hl=en"
# A browser UA is required; the default urllib agent is refused outright.
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)


def read_current() -> dict[str, str]:
    """Parse the existing YAML well enough to preserve keys we do not compute."""
    values: dict[str, str] = {}
    if not DATA.exists():
        return values
    for line in DATA.read_text().splitlines():
        m = re.match(r'^([a-z_]+):\s*"?([^"#]*?)"?\s*$', line)
        if m:
            values[m.group(1)] = m.group(2).strip()
    return values


def count_publications() -> int | None:
    if not BIB.exists():
        return None
    # Count entry headers only; @string/@comment are not publications.
    return len(re.findall(r"^@(?!string|comment|preamble)\w+\s*\{", BIB.read_text(), re.M | re.I))


def fetch_metrics(uid: str) -> tuple[int, int]:
    """Return (citations_all, h_index_all). Raises on any parsing problem."""
    req = urllib.request.Request(PROFILE.format(uid=uid), headers={"User-Agent": UA})
    html = urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "ignore")

    if "gsc_rsb_std" not in html:
        # Almost always the CAPTCHA interstitial rather than a layout change.
        raise ValueError("no stats table in response (likely rate-limited or CAPTCHA)")

    # The summary table is six cells: citations all/since, h-index all/since,
    # i10 all/since. We want the two "all" columns.
    cells = [int(c) for c in re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', html)]
    if len(cells) < 3:
        raise ValueError(f"expected >=3 stat cells, found {len(cells)}")

    citations, h_index = cells[0], cells[2]
    if citations <= 0 or h_index <= 0:
        raise ValueError(f"implausible values: citations={citations} h_index={h_index}")
    return citations, h_index


def main() -> int:
    current = read_current()
    uid = current.get("scholar_id") or "_d2LuhQAAAAJ"

    pubs = count_publications()
    if pubs is None:
        print(f"WARN  bibliography not found at {BIB}", file=sys.stderr)
        pubs = int(current.get("publications") or 0) or None

    try:
        citations, h_index = fetch_metrics(uid)
    except (urllib.error.URLError, ValueError, TimeoutError, OSError) as exc:
        print(f"WARN  Google Scholar fetch failed: {exc}", file=sys.stderr)
        print("WARN  leaving _data/scholar.yml unchanged (last good values kept)", file=sys.stderr)
        return 0

    today = dt.date.today()
    fields = {
        "citations": str(citations),
        "citations_display": f'"{citations:,}"',
        "h_index": str(h_index),
        "publications": str(pubs if pubs else current.get("publications", "0")),
        "scholar_id": uid,
        "updated": f'"{today.isoformat()}"',
        "updated_display": f'"{today.strftime("%-d %B %Y")}"',
    }

    header = DATA.read_text().split("\ncitations:")[0] if DATA.exists() else ""
    body = "\n".join(f"{k}: {v}" for k, v in fields.items())
    DATA.write_text(f"{header}\n{body}\n" if header else f"{body}\n")

    print(f"OK    citations={citations:,} h_index={h_index} publications={fields['publications']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

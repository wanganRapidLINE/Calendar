#!/usr/bin/env python3
"""Regenerate the bundled Japanese public holiday table.

The Cabinet Office publishes the authoritative list of national holidays as a
Shift_JIS CSV.  It covers 1955 up to the end of the following year - the
equinox days cannot be published any earlier because they are fixed by
astronomical observation and only become law in February of the preceding
year.  So this needs re-running once a year, some time after February.

    python tools/UpdateJapaneseHolidays.py

Writes app/src/main/res/raw/japanese_holidays.csv as "yyyyMMdd,name" lines,
UTF-8, sorted by date.  The date format matches the dayCode strings the app
already uses internally, so the app can look holidays up without parsing.
"""

import argparse
import csv
import io
import pathlib
import sys
import urllib.request

SOURCE_URL = "https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv"
SOURCE_ENCODING = "cp932"
OUTPUT_PATH = pathlib.Path(__file__).resolve().parents[1] / "app/src/main/res/raw/japanese_holidays.csv"


def fetch(url: str) -> str:
    with urllib.request.urlopen(url, timeout=60) as response:
        return response.read().decode(SOURCE_ENCODING)


def parse(text: str) -> list[tuple[str, str]]:
    rows = csv.reader(io.StringIO(text))
    header = next(rows, None)
    if header is None or "月日" not in header[0]:
        raise ValueError(f"unexpected header, the CSV layout may have changed: {header}")

    holidays = []
    for row in rows:
        if len(row) < 2 or not row[0].strip():
            continue
        year, month, day = (int(part) for part in row[0].strip().split("/"))
        name = row[1].strip()
        holidays.append((f"{year:04d}{month:02d}{day:02d}", name))

    holidays.sort()
    return holidays


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", help="read a locally saved copy of the CSV instead of downloading it")
    args = parser.parse_args()

    if args.input:
        text = pathlib.Path(args.input).read_text(encoding=SOURCE_ENCODING)
    else:
        print(f"downloading {SOURCE_URL}")
        text = fetch(SOURCE_URL)

    holidays = parse(text)
    if not holidays:
        print("no holidays parsed, refusing to write an empty table", file=sys.stderr)
        return 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="\n") as output:
        for day_code, name in holidays:
            output.write(f"{day_code},{name}\n")

    print(f"wrote {len(holidays)} holidays ({holidays[0][0]} - {holidays[-1][0]}) to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Command line entry point.

Usage: python3 -m gorman_oee.cli --plant DET data/detroit_shift_log.csv
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from .adapters import ADAPTERS
from .calculator import calculate_shift, weighted_plant_oee
from .model import InvalidShiftRecordError

EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_ERROR = 2

logger = logging.getLogger("gorman_oee")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Gorman standard OEE (GMS-OPS-007)")
    parser.add_argument("--plant", required=True, choices=sorted(ADAPTERS))
    parser.add_argument("export", type=Path, help="Plant export file")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    if not args.export.is_file():
        logger.error("Export file not found: %s", args.export)
        return EXIT_ERROR

    try:
        results = [calculate_shift(r) for r in ADAPTERS[args.plant](args.export)]
    except (InvalidShiftRecordError, KeyError, ValueError) as exc:
        logger.error("Rejected export %s: %s", args.export, exc)
        return EXIT_FAILURE

    for result in results:
        flags = ",".join(sorted(f.value for f in result.flags)) or "-"
        print(f"{result.record.key:<28} OEE {result.oee_percent:5.1f}%  flags={flags}")
    print(f"{args.plant} plant OEE (weighted by planned time): {weighted_plant_oee(results)}%")
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())

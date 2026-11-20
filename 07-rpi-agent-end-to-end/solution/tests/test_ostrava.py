"""Ostrava (OSR) adapter tests. Run: python3 -m unittest discover -s tests -t ."""

import unittest
from pathlib import Path

from gorman_oee import calculate_shift
from gorman_oee.adapters import ADAPTERS, read_ostrava

DATA = Path(__file__).resolve().parents[1] / "data"


class OstravaAdapterTests(unittest.TestCase):
    def setUp(self):
        self.records = list(read_ostrava(DATA / "ostrava_shift_export.json"))

    def test_registered(self):
        self.assertIs(ADAPTERS["OSR"], read_ostrava)

    def test_golden_shift(self):
        golden = next(r for r in self.records if r.line == "L1" and r.shift == "A")
        self.assertEqual(calculate_shift(golden).oee_percent, 77.2)

    def test_rework_is_not_good(self):
        golden = next(r for r in self.records if r.shift == "A")
        self.assertEqual(golden.good_count, 780 - 25 - 14)

    def test_units_converted(self):
        golden = self.records[0]
        self.assertEqual((golden.planned_minutes, golden.downtime_minutes, golden.ideal_cycle_seconds), (480, 47, 30))


if __name__ == "__main__":
    unittest.main()

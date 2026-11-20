"""Tests for the Gorman OEE library. Run: python3 -m unittest discover -s tests -t ."""

import unittest
from pathlib import Path

from gorman_oee import InvalidShiftRecordError, OeeFlag, ShiftRecord, calculate_shift, weighted_plant_oee
from gorman_oee.adapters import read_detroit, read_monterrey, read_pune

DATA = Path(__file__).resolve().parents[1] / "data"
GOLDEN_OEE = 77.2  # GMS-OPS-007 worked example: Line 1, shift A, 2026-11-02


def make(**overrides):
    values = dict(
        plant="DET", line="L1", shift_date="2026-11-02", shift="A",
        planned_minutes=480, downtime_minutes=47, ideal_cycle_seconds=30,
        total_count=780, good_count=741,
    )
    values.update(overrides)
    return ShiftRecord(**values)


class CalculatorTests(unittest.TestCase):
    def test_golden_shift_matches_standard(self):
        self.assertEqual(calculate_shift(make()).oee_percent, GOLDEN_OEE)

    def test_no_production_returns_zero_and_flag(self):
        result = calculate_shift(make(downtime_minutes=480, total_count=0, good_count=0))
        self.assertEqual(result.oee_percent, 0.0)
        self.assertIn(OeeFlag.NO_PRODUCTION, result.flags)

    def test_performance_over_100_is_flagged(self):
        result = calculate_shift(make(ideal_cycle_seconds=60))
        self.assertIn(OeeFlag.PERF_OVER_100, result.flags)

    def test_invalid_records_are_rejected(self):
        for bad in ({"downtime_minutes": 500}, {"good_count": 800}, {"total_count": -1}):
            with self.subTest(bad=bad), self.assertRaises(InvalidShiftRecordError):
                make(**bad)

    def test_plant_average_is_weighted_by_planned_time(self):
        long_shift = calculate_shift(make(planned_minutes=600, downtime_minutes=0, ideal_cycle_seconds=60,
                                          total_count=600, good_count=600))
        short_shift = calculate_shift(make(planned_minutes=200, downtime_minutes=200, total_count=0, good_count=0))
        self.assertEqual(weighted_plant_oee([long_shift, short_shift]), 75.0)


class AdapterTests(unittest.TestCase):
    """The same physical shift must give the same OEE in every plant format."""

    def golden(self, records):
        return next(r for r in records if r.line == "L1" and r.shift == "A")

    def test_every_plant_format_gives_golden_oee(self):
        readers = {
            "detroit": (read_detroit, "detroit_shift_log.csv"),
            "monterrey": (read_monterrey, "monterrey_registro_turnos.csv"),
            "pune": (read_pune, "pune_shift_export.csv"),
        }
        for plant, (reader, filename) in readers.items():
            with self.subTest(plant=plant):
                record = self.golden(reader(DATA / filename))
                self.assertEqual(calculate_shift(record).oee_percent, GOLDEN_OEE)


if __name__ == "__main__":
    unittest.main()

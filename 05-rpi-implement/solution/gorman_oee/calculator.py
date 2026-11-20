"""OEE calculation per Gorman standard GMS-OPS-007 rev C."""

from __future__ import annotations

from collections.abc import Iterable

from .model import OeeFlag, OeeResult, ShiftRecord


def calculate_shift(record: ShiftRecord) -> OeeResult:
    """Return full-precision OEE factors for one shift.

    Zero production or zero run time gives OEE 0.0 with the NO_PRODUCTION flag (rule 2).
    """
    if record.total_count == 0 or record.run_minutes == 0:
        availability = record.run_minutes / record.planned_minutes
        return OeeResult(record, availability, 0.0, 0.0, frozenset({OeeFlag.NO_PRODUCTION}))

    availability = record.run_minutes / record.planned_minutes
    performance = (record.ideal_cycle_seconds * record.total_count) / (record.run_minutes * 60)
    quality = record.good_count / record.total_count

    flags = frozenset({OeeFlag.PERF_OVER_100}) if performance > 1.0 else frozenset()
    return OeeResult(record, availability, performance, quality, flags)


def weighted_plant_oee(results: Iterable[OeeResult]) -> float:
    """Plant OEE weighted by planned time (rule 5), as a rounded percentage."""
    results = list(results)
    total_planned = sum(r.record.planned_minutes for r in results)
    if total_planned == 0:
        return 0.0
    weighted = sum(r.oee * r.record.planned_minutes for r in results) / total_planned
    return round(weighted * 100, 1)

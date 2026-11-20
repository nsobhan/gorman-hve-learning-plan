"""Canonical data model for Gorman shift OEE (standard GMS-OPS-007 rev C)."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class OeeFlag(str, Enum):
    """Data-quality flags attached to a calculated shift."""

    NO_PRODUCTION = "NO_PRODUCTION"
    PERF_OVER_100 = "PERF_OVER_100"


class InvalidShiftRecordError(ValueError):
    """Raised when a shift record breaks the validation rules in GMS-OPS-007."""


@dataclass(frozen=True)
class ShiftRecord:
    """One shift on one line, normalized to Gorman standard units."""

    plant: str
    line: str
    shift_date: str  # ISO 8601 date, e.g. 2026-11-02
    shift: str
    planned_minutes: float
    downtime_minutes: float
    ideal_cycle_seconds: float
    total_count: int
    good_count: int

    def __post_init__(self) -> None:
        numeric = {
            "planned_minutes": self.planned_minutes,
            "downtime_minutes": self.downtime_minutes,
            "ideal_cycle_seconds": self.ideal_cycle_seconds,
            "total_count": self.total_count,
            "good_count": self.good_count,
        }
        negatives = [name for name, value in numeric.items() if value < 0]
        if negatives:
            raise InvalidShiftRecordError(f"{self.key}: negative values in {negatives}")
        if self.planned_minutes == 0:
            raise InvalidShiftRecordError(f"{self.key}: planned_minutes must be greater than 0")
        if self.downtime_minutes > self.planned_minutes:
            raise InvalidShiftRecordError(f"{self.key}: downtime exceeds planned time")
        if self.good_count > self.total_count:
            raise InvalidShiftRecordError(f"{self.key}: good_count exceeds total_count")

    @property
    def key(self) -> str:
        return f"{self.plant}/{self.line}/{self.shift_date}/{self.shift}"

    @property
    def run_minutes(self) -> float:
        return self.planned_minutes - self.downtime_minutes


@dataclass(frozen=True)
class OeeResult:
    """Full-precision OEE factors for one shift."""

    record: ShiftRecord
    availability: float
    performance: float
    quality: float
    flags: frozenset[OeeFlag] = field(default_factory=frozenset)

    @property
    def oee(self) -> float:
        return self.availability * self.performance * self.quality

    @property
    def oee_percent(self) -> float:
        """OEE rounded once, at the end, to one decimal place (rule 1)."""
        return round(self.oee * 100, 1)

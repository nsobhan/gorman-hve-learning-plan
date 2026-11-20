"""Plant adapters: convert each plant's current export format into ShiftRecord.

Plant exports can't change this quarter (problem statement constraint), so each
adapter accepts today's format exactly as it is.
"""

from __future__ import annotations

import csv
import json
from collections.abc import Callable, Iterator
from pathlib import Path

from .model import ShiftRecord

# Pune shift starts (UTC) mapped to the local shift letter.
_PUNE_SHIFT_BY_UTC_HOUR = {"00": "A", "08": "B", "16": "C"}


def read_detroit(path: Path) -> Iterator[ShiftRecord]:
    """Detroit: comma CSV, minutes, English headers."""
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            yield ShiftRecord(
                plant=row["Plant"],
                line=row["LineID"],
                shift_date=row["Date"],
                shift=row["Shift"],
                planned_minutes=float(row["PlannedMin"]),
                downtime_minutes=float(row["DownMin"]),
                ideal_cycle_seconds=float(row["IdealCycleSec"]),
                total_count=int(row["TotalParts"]),
                good_count=int(row["GoodParts"]),
            )


def read_monterrey(path: Path) -> Iterator[ShiftRecord]:
    """Monterrey: comma CSV, hours, Spanish headers."""
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            yield ShiftRecord(
                plant=row["planta"],
                line=row["linea"],
                shift_date=row["fecha"],
                shift=row["turno"],
                planned_minutes=float(row["horas_planeadas"]) * 60,
                downtime_minutes=float(row["horas_paro"]) * 60,
                ideal_cycle_seconds=float(row["ciclo_ideal_seg"]),
                total_count=int(row["piezas_totales"]),
                good_count=int(row["piezas_buenas"]),
            )


def read_pune(path: Path) -> Iterator[ShiftRecord]:
    """Pune: semicolon CSV, seconds and milliseconds, reject count instead of good count."""
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter=";"):
            start = row["shift_start_utc"]
            produced = int(row["produced"])
            yield ShiftRecord(
                plant=row["plant_code"],
                line=row["line"],
                shift_date=start[:10],
                shift=_PUNE_SHIFT_BY_UTC_HOUR.get(start[11:13], start[11:16]),
                planned_minutes=int(row["planned_sec"]) / 60,
                downtime_minutes=int(row["downtime_sec"]) / 60,
                ideal_cycle_seconds=int(row["ideal_cycle_ms"]) / 1000,
                total_count=produced,
                good_count=produced - int(row["rejected"]),
            )


# Ostrava (OSR) unit conversions to canonical minutes and seconds.
_TO_MINUTES = {"h": 60.0, "min": 1.0, "s": 1 / 60}
_TO_SECONDS = {"min": 60.0, "s": 1.0, "ms": 0.001}


def read_ostrava(path: Path) -> Iterator[ShiftRecord]:
    """Ostrava: JSON export v2.x, hours and minutes, downtime as a list of stops.

    Good count is first-pass good only (GMS-OPS-007): total - scrap - rework.
    """
    export = json.loads(path.read_text(encoding="utf-8"))
    for shift in export["shifts"]:
        planned = shift["plannedTime"]
        cycle = shift["idealCycle"]
        counts = shift["counts"]
        yield ShiftRecord(
            plant=export["site"],
            line=shift["line"],
            shift_date=shift["date"],
            shift=shift["shift"],
            planned_minutes=planned["value"] * _TO_MINUTES[planned["unit"]],
            downtime_minutes=sum(stop["minutes"] for stop in shift["unplannedStops"]),
            ideal_cycle_seconds=cycle["value"] * _TO_SECONDS[cycle["unit"]],
            total_count=counts["total"],
            good_count=counts["total"] - counts["scrap"] - counts["rework"],
        )


ADAPTERS: dict[str, Callable[[Path], Iterator[ShiftRecord]]] = {
    "DET": read_detroit,
    "MTY": read_monterrey,
    "PNQ": read_pune,
    "OSR": read_ostrava,
}

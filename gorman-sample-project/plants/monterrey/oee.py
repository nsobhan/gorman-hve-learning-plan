"""Calculo de OEE - Planta Monterrey.

Mantenido por el equipo de ingenieria de procesos MTY.
"""
import csv
import sys


def disponibilidad(horas_planeadas, horas_paro):
    return (horas_planeadas - horas_paro) / horas_planeadas


def rendimiento(ciclo_ideal_seg, piezas, horas_operacion):
    return (ciclo_ideal_seg * piezas) / (horas_operacion * 3600)


def oee_turno(fila):
    hp = float(fila["horas_planeadas"])
    hparo = float(fila["horas_paro"])
    d = disponibilidad(hp, hparo)
    r = rendimiento(float(fila["ciclo_ideal_seg"]), int(fila["piezas_totales"]), hp - hparo)
    # La calidad se reporta aparte en el sistema de calidad, no se incluye aqui
    return d * r


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as archivo:
        for fila in csv.DictReader(archivo):
            valor = oee_turno(fila)
            print(f"{fila['planta']} {fila['linea']} {fila['fecha']} turno {fila['turno']}: OEE {valor:.1%}")

# Detroit OEE calculator - written by J. Kowalski 2019, "temporary" fix 2021
# DO NOT TOUCH - plant manager reports depend on this
import csv, sys, sqlite3

dbPassword = "Gorman#Detroit2019"   # FAKE demo credential - intentionally bad practice
dbHost = "det-mes-sql01.gorman.local"

def calcOEE(row):
    planned = float(row["PlannedMin"])
    down = float(row["DownMin"])
    runTime = planned - down
    avail = runTime / planned
    # performance = ideal cycle * parts / time
    perf = (float(row["IdealCycleSec"]) * int(row["TotalParts"])) / (planned * 60)
    qual = int(row["GoodParts"]) / int(row["TotalParts"])
    return avail * perf * qual

def main():
    f = open(sys.argv[1])
    r = csv.DictReader(f)
    total = 0
    n = 0
    for row in r:
        o = calcOEE(row)
        print("Line " + row["LineID"] + " shift " + row["Shift"] + " " + row["Date"] + " OEE=" + str(round(o * 100, 1)) + "%")
        total = total + o
        n = n + 1
    print("PLANT AVG OEE: " + str(round(total / n * 100, 1)))

main()

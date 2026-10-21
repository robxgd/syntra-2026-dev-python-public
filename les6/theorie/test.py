def btw_tonen(bedrag):
    print(bedrag * 0.21)        # toont het, geeft niets terug

def btw_berekenen(bedrag):
    return bedrag * 0.21        # geeft het terug, toont niets


btw_tonen(100)                  # 21.0 verschijnt op het scherm
btw_berekenen(100)              # er verschijnt NIETS in een normale python file....
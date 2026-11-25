zin = "  De snelle bruine vos springt over de luie hond  "

# A spaties weghalen
zin = zin.strip()
print(zin)

# Splitten 
woorden = zin.split()
print(woorden)

# B1: aantal tekens
print(f"Tekens: {len(zin)}")

# B2: aantal woorden
print(f"Woorden: {len(woorden)}")

# C eerste en laatste woord
print(woorden[0])
print(woorden[-1])

# D upper en lower
print(zin.upper())
print(zin.lower())

# E zit een woord er in 
print("vos" in woorden)
print("kat" in woorden)
print("vos" in zin) # opletten, als je checkt in zin kan het ook een subwoord zijn (bv: vosje)
print("kat" in zin)

# F print elk woord met een nummer
for nummer, woord in enumerate(woorden, start=1):
    print(f"{nummer}. {woord}")
# andere optie voor hetzelfde probleem 
teller = 1
for woord in woorden:
    print(f"{teller}, {woord}")
    teller +=1

# Spaties en hoofdletters veroorzaken allebei een verschil.
antwoord = "  JA  "
print(antwoord == "ja")
print(antwoord.strip().lower() == "ja")

# Extra 1
for woord in woorden:
    if len(woord) > 4:
        print(woord)

# Extra 2
print(" ".join(woorden[::-1]))

teller = 1
result = ""
for woord in woorden:
    if(teller == 1):
        result = woorden[len(woorden)-teller]
    else:
        result = result + " "+woorden[len(woorden)-teller] 
    teller = teller+1
print(result)

zin = "de kat zat op de mat en de kat sliep"

# A hoeveel woorden
woorden = zin.split()
print(f"Aantal woorden: {len(woorden)}")



# B tellingen bijhouden van frequentie woord
tellingen = {}
for woord in woorden:
    tellingen[woord] = tellingen.get(woord, 0) + 1
print(tellingen)

# C aantal unieke woorden 
print(f"Unieke woorden: {len(tellingen)}")

# D aantal woorden die meerdere keren voorkomen
for woord, aantal in tellingen.items():
    if aantal > 1:
        print(f"{woord} komt {aantal} keer voor")

# E
beste_woord = ""
beste_aantal = 0
for woord, aantal in tellingen.items():
    if aantal >= beste_aantal:
        beste_woord = woord
        beste_aantal = aantal
# Bij gelijkstand wint het eerst aangetroffen woord.
if tellingen:
    print(f"Meest voorkomend: {beste_woord} met {beste_aantal}")
else:
    print("Geen woorden.")

# Extra: hoofdletters en punten normaliseren voor de tweede testzin.
zin = "De kat zat op de mat. De KAT sliep."
schoon = zin.lower().replace(".", "")
print(schoon)
tellingen = {}
for woord in schoon.split():
    tellingen[woord] = tellingen.get(woord, 0) + 1
print(tellingen)

# Extra: alleen letters tellen, geen spaties of leestekens.
letters = {}
for letter in schoon:
    if letter.isalpha():
        letters[letter] = letters.get(letter, 0) + 1
print(letters)

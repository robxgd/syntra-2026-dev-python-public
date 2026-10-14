"""OPLOSSING 3: totaal en gemiddelde."""

bonnen = [10, 15, 12, 8, 15]

# De startwaarde staat VOOR de lus. Staat ze erin, dan reset ze elke ronde
# (zie fout_1_som.py).
totaal = 0
for bon in bonnen:
    totaal = totaal + bon

# Bonus: bij een lege lijst zou dit delen door nul zijn
if len(bonnen) == 0:
    print("Geen bonnen")
else:
    gemiddelde = totaal / len(bonnen)
    print(f"Totaal: {totaal}")
    print(f"Gemiddelde: {gemiddelde}")

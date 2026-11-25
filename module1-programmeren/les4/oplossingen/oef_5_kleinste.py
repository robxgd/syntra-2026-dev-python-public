"""OPLOSSING 5: de kleinste waarde zoeken."""

temperaturen = [3, -2, 7, -9, 0, 5]

# Startwaarde = een echt element uit de lijst. Met 0 zou een lijst met
# alleen positieve getallen fout gaan (0 is dan "te klein" en blijft staan).
laagste = temperaturen[0]

for temperatuur in temperaturen:
    if temperatuur < laagste:
        laagste = temperatuur

print(f"Laagste temperatuur: {laagste}")

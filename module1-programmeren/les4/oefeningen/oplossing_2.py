# 1. vraag hoeveel producten er zijn
aantal_producten = int(input("hoeveel producten zijn er: "))

# 2. lees de prijzen één voor één in en bewaar ze in een lijst
prijslijst = []
aantal = 0
while aantal < aantal_producten:
    prijs = float(input("geef prijs product: "))
    prijslijst.append(prijs)
    aantal+=1


# 3. tel de prijzen op
# totaal = sum(prijslijst)
totaal = 0
for item in prijslijst:
    totaal = totaal + item
print(totaal)

# 4. zoek de duurste prijs
max = prijslijst[0]
for prijs in prijslijst: 
    if(max < prijs):
        max = prijs
print(f"de max prijs is: {max}")


# 5. bereken het gemiddelde
# totaal = 0
# for prijs in prijslijst: 
#     totaal = totaal + prijs
gemiddelde = totaal/aantal

# 6. toon aantal, totaal, duurste en gemiddelde

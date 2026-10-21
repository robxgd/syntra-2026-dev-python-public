temperaturen = [12, 18, 7, 21, 15, 9, 24]

# A som van alle temperaturen 
som = 0 
for temp in temperaturen:
    som = som + temp
print(som)


# B gemiddelde

gemiddelde = som / len(temperaturen)
print(f"het gemiddelde is: {gemiddelde:.2f}")


# C hoogste waarde
temperaturen.sort(reverse=True)
print(temperaturen[0])

hoogste_temp = temperaturen[0]
for temp in temperaturen:
    if(temp > hoogste_temp):
        hoogste_temp = temp

print("hoogste temperatuur: ", hoogste_temp)

# D Tel de dagen hoger dan 15 graden 
aantal_boven_15 = 0
for temp in temperaturen: 
    if(temp>=15):
        aantal_boven_15 = aantal_boven_15 + 1

print(f"er zijn in totaal: {aantal_boven_15} warme dagen.")
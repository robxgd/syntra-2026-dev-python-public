
voorraad_raw = {"appel": 12, "peer": 5, "banaan": 0}

class Fruit:
    def __init__(self, naam, aantal):
        self.naam = naam
        self.aantal = aantal
    def toon(self):
        print(f"{self.naam}: {self.aantal}")

class Voorraad:
    def __init__(self, fruit=None):
        self.fruit = fruit if fruit is not None else []
    def totaal_aantal_stukken(self):
        totaal = 0
        for fruit in self.fruit: 
            totaal += fruit.aantal
        return totaal
    def voeg_toe(self, fruit):
        self.fruit.append(fruit)

# fruitjes = []
voorraad = Voorraad()
for key, value in voorraad_raw.items():
    voorraad.voeg_toe(Fruit(key, value))

    # fruitjes.append(fruit)

voorraad.voeg_toe(Fruit("peren", 5))

# voorraad = Voorraad(fruitjes)
print(voorraad.totaal_aantal_stukken())
# for fruit in fruitjes:
#     fruit.toon()
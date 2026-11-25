"""OPLOSSING 8: while."""

doel = 450
saldo = 120
maandelijks = 75
maanden = 0

while saldo < doel:
    saldo = saldo + maandelijks
    maanden = maanden + 1
    print(f"Maand {maanden}: {saldo} euro")

print(f"Je kan de fiets kopen na {maanden} maanden.")

# Bonus: met maandelijks = 0 verandert saldo nooit, de voorwaarde blijft
# waar en de lus stopt nooit (oneindige lus).

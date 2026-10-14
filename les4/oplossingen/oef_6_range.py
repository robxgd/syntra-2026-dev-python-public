"""OPLOSSING 6: range()."""

print("Tafel van 7:")
for i in range(1, 11):          # stopt VOOR 11
    print(f"7 x {i} = {7 * i}")

som = 0
for i in range(1, 101):
    som = som + i
print(f"Som van 1 tot en met 100: {som}")

print("Even getallen tot 20: ", end="")
for i in range(2, 21, 2):       # derde argument: stapgrootte
    print(i, end=" ")
print()                         # sluit de regel af

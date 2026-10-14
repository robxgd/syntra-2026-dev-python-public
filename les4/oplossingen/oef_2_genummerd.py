"""OPLOSSING 2: een lijst afdrukken met een lus."""

deelnemers = ["Sofie", "Ahmed", "Lotte", "Jonas"]

for plaats, naam in enumerate(deelnemers, start=1):
    print(f"{plaats}. {naam}")

# Niet ingesprongen: gebeurt één keer, na de lus
print(f"Klaar: {len(deelnemers)} deelnemers")

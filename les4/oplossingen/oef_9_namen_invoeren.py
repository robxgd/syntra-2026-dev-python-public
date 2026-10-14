"""OPLOSSING 9: alles samen."""

namen = []

while True:
    naam = input("Naam (of stop): ")
    if naam == "stop":
        break
    namen.append(naam)

if len(namen) == 0:
    print("Geen namen ingegeven")
else:
    print(f"Je gaf {len(namen)} namen in:")
    for plaats, naam in enumerate(namen, start=1):
        print(f"{plaats}. {naam}")

    langste = namen[0]
    for naam in namen:
        if len(naam) > len(langste):    # strikt groter: bij gelijkstand wint de eerste
            langste = naam
    print(f"De langste naam is {langste}")

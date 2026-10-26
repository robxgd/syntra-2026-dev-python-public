# Oefening 3: Repareer de fout

> ± 20 minuten · individueel · drie bestanden in deze map

Drie programma's met functies. Zelfde werkwijze: **hypothese eerst als commentaar, dan
uitvoeren, dan pas fixen.** Noteer ook als commentaar wat er echt misging en of je hypothese
klopte.

---

| Bestand | Zou moeten geven |
|---|---|
| `fout_1_geen_return.py` | `De btw bedraagt 21.0 euro` |
| `fout_2_scope.py` | `Totaal: 60` |
| `fout_3_argumenten.py` | `Na korting: 90.0 euro` |

## De derde is de gemene

`fout_1` en `fout_2` crashen met een foutmelding die je erheen wijst. `fout_3` draait gewoon
door en toont een bedrag.

Kijk goed naar de volgorde van de parameters in de functie, en naar de volgorde waarin ze
worden meegegeven bij de oproep.

> Hoe zou je deze fout onmogelijk kunnen maken bij het oproepen?
> Tip: zoek op wat `korting(bedrag=100, procent=10)` doet.

## Klaar en tijd over?

Neem `fout_2_scope.py` na je reparatie en probeer dit:

```python
totaal = 999
tel_op([10, 20, 30])
print(totaal)
```

Wat verwacht je? En wat gebeurt er? Verklaar het in één zin.

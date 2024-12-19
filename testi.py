salasana = int(input("Anna salasana 5 numeroinen salasana: "))

print("Olen pian valmis, salasanan etsintä käynnissä...")

for luku in range(0, 100000):
    if luku == salasana:
        print(f"Salasanasi on {luku}")
#Extra teksti
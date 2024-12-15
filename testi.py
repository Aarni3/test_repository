salasana = int(input("Anna salasana 7 numeroinen salasana: "))

print("Olen pian valmis, salasanan etsintä käynnissä...")

for luku in range(0, 10000000):
    if luku == salasana:
        print(f"Salasanasi on {luku}")

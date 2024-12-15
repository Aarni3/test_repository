salasana = int(input("Anna salasana 3 numeroinen salasana: "))

print("Salasanan etsintä käynnissä...")

for luku in range(0, 1000):
    if luku == salasana:
        print(f"Salasanasi on {luku}")

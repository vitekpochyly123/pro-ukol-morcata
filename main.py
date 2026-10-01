with open("morcata.txt", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            j, h, d, c, p = line.strip().split(";")
            typ = "Sameček" if p.lower() == "m" else "Samička"
            print(f"{typ} morčete jménem: {j}")
            print(f"- váží: {h} g")
            print(f"- datum narození: {d}")
            print(f"- cena se slevou 10 %: {float(c)*0.9:.1f} Kč\n")
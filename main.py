# Kérj be a felhasználótól egy szöveget.  Alakítsd nagybetűssé!

    szoveg1 = str(input("Kérem adjon meg egy szöveget!"))
    nagybetu = szoveg1.upper()
    print(nagybetu)

# Az előző szövegről döntsd el, hogy 10 karakternél hosszabb-e? Ha igen, akkor írd ki a hosszát!
    if len(szoveg1) < 10:
        print("Ez a szöveg nem éri el a 10 karaktert.")
    else:
        print(f"Ez a szöveg {len(szoveg1)} karakter hosszú.")


# Kérj be egy legalább 3 betűs szót a felhasználótól. A szavakat addig kérd be, amíg a hossza legalább 3!

    szo = str(input("Kérem adjon megy egy 3 betűs szót."))
    while len(szo) <= 3:
        szo = str(input("Ez nem 3 betűs, kérem adjon meg mást!."))
    print(f"A megadott szó {szo}.")


# Kérj be a felhasználótól egy szöveget. Keresd meg benne az első "a" betűt.

    szoveg = str(input("Kérem adjon meg egy szöveget!"))
    i = 0
    while i < len(szoveg) and szoveg[i].upper() != 'A':
        i += 1
    if i < len(szoveg):
        print(f"Van |a| betű a szövegben {i + 1} karakteren")
    else:
        print("Nincs a szövegben |a| betű")


# Hány "a" betű van a bekért szövegben?

    szoveg = str(input("Kérem adjon meg egy szöveget!"))
    i = 0
    while i < len(szoveg) and szoveg[i] != "a":
        i += 1

    if i <= len(szoveg):

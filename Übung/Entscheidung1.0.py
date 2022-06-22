eingabe = float(input("gimme a number:"))  # input erzeugt immer strings!
grenzwert_unten = float(input("Welcher untere Grenzwert?"))
grenzwert_oben = float(input("Welcher obere Grenzwert?"))

if grenzwert_unten <= eingabe <= grenzwert_oben:
    print("Zahl ist im Bereich")
else:
    print("Zahl ist gleich Grenzwert")
eingabe = input('Bitte eine Zahl eingeben = ')
zahl = float(eingabe)
low = 42
high = 69
if zahl >= low and zahl <= high:
    print("im Bereich")
    if zahl == 69:
        print("69. That's the funny number.")
    else:
        print("done")
else:
    print("nicht im Bereich")
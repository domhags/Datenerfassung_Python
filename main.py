def ausgabe_daten():
    # Abfrage zur Ausgabe der Daten
    print("Möchten Sie die Daten ausgeben lassen?\nj für Ja, n für Nein")
    auswahl = input()
    if auswahl == "j":
        # Ausgabe aller gespeicherten Datensätze zum Testen, ob die Werte gespeichert wurden
        for person in gespeicherteDaten:
            print(person, sep="\n")
    else:
        print("Das Programm wird beendet!")

personenDaten = ["Vorname: ", "Nachname: ", "Straße: ", "PLZ: ", "Ort: "]  # Liste der Datenfelder
gespeicherteDaten = []  # Liste zum Speichern aller Datensätze

print("Herzlich Willkommen zur Datenerfassung.")
print("Bitte geben Sie die Personendaten ein:")
print()

# Hauptschleife zur Dateneingabe
while True:
    for person in personenDaten:
        print(person)  # Benutzer zur Eingabe des aktuellen Datenfelds auffordern
        daten = input()  # Benutzereingabe erfassen

        while daten == "":
            print("Feld darf nicht leer sein!")
            print(person)
            daten = input()

        gespeicherteDaten.append(daten)

    # Benutzer nach weiteren Dateneingaben fragen
    print("Wollen Sie weitere Daten eingeben?\nj für Ja, n für Nein")
    eingabe = input()

    if eingabe == "j":
        continue
    elif eingabe == "n":
        ausgabe_daten()
        break
    else:
        print("Falsche Eingabe! Geben Sie j für ja oder n für nein ein")
        break








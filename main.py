def ausgabe_daten():
    # Abfrage zur Ausgabe der Daten
    while True:
        auswahl = input("Möchten Sie die Daten ausgeben lassen?\nj für Ja, n für Nein\n")
        if auswahl == "j":
            for personen in gespeicherteDaten:
                print(personen)  # Hier werden alle Elemente in einer Liste ausgegeben
        elif auswahl == "n":
            print("Das Programm wird beendet!")
            exit()
        else:
            print("Ungültige Eingabe. Bitte geben Sie j für j, n für Nein ein!")


# Hier beginnt der Main-Teil
bezeichnerDaten = ["Vorname: ", "Nachname: ", "Straße: ", "PLZ: ", "Ort: "]  # Liste der Datenfelder
gespeicherteDaten = []  # Liste zum Speichern aller Datensätze

print("Herzlich Willkommen zur Datenerfassung.\nBitte geben Sie die Personendaten ein:\n")

# Hauptschleife zur Dateneingabe
while True:
    personenListe = []
    for person in bezeichnerDaten:
        daten = input(person)  # Benutzereingabe erfassen

        while daten == "":
            daten = input("Feld darf nicht leer sein!\n" + person)

        personenListe.append(daten)

    gespeicherteDaten.append(personenListe.copy())  # Eine Kopie von personenListe wird hinzugefügt
    personenListe.clear()  # personenListe wird gelöscht.

    # Benutzer nach weiteren Dateneingaben fragen
    while True:
        eingabe = input("Wollen Sie weitere Daten eingeben?\nj für Ja, n für Nein\n")

        if eingabe == "j":
            break
        elif eingabe == "n":
            ausgabe_daten()
        else:
            print("Falsche Eingabe! Geben Sie j für ja oder n für nein ein\n")

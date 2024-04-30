personenDaten = ["Vorname: ", "Nachname: ", "Straße: ", "PLZ: ", "Ort: "]  # Liste der Datenfelder
gespeicherteDaten = []  # Liste zum Speichern aller Datensätze

print("Herzlich Willkommen zur Datenerfassung.")
print("Bitte geben Sie die Personendaten ein:")
print()

# Hauptschleife zur Dateneingabe
while True:
    daten_eingabe = []  # Liste zum Speichern der Eingabedaten für einen Datensatz

    for x in personenDaten:
        print(x)  # Benutzer zur Eingabe des aktuellen Datenfelds auffordern
        daten = input()  # Benutzereingabe erfassen

        if daten != "":
            daten_eingabe.append(daten)
        else:
            print("Feld darf nicht leer sein")
            break

    # Überprüfen, ob Daten im aktuellen Datensatz vorhanden sind
    if daten_eingabe:
        gespeicherteDaten.append(daten_eingabe)  # Den aktuellen Datensatz speichern

    # Benutzer nach weiteren Dateneingaben fragen
    print("Wollen Sie weitere Daten eingeben?")
    print("j für Ja, n für Nein")
    eingabe = input()

    if eingabe == "n":
        break
    elif eingabe == "j":
        continue
    else:
        print("Falsche Eingabe!")
        break

# Ausgabe aller gespeicherten Datensätze zum Testen, ob die Werte gespeichert wurden
for person in gespeicherteDaten:
    for (x, y) in zip(personenDaten, person):
        print(x, y)
    print()

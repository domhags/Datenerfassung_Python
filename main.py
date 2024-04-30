# Definition der Ausgangsvariablen
personenDaten = ["Vorname: ", "Nachname: ", "Straße: ", "PLZ: ", "Ort: "]  # Liste der Datenfelder
gespeicherteDaten = []  # Liste zum Speichern aller Datensätze

# Begrüßungsnachricht
print("Herzlich Willkommen zur Datenerfassung.")
print("Bitte geben Sie die Personendaten ein:")
print()

# Hauptschleife zur Dateneingabe
while True:
    daten_eingabe = []  # Liste zum Speichern der Eingabedaten für einen Datensatz

    # Schleife für jedes Datenfeld
    for x in personenDaten:
        print(x)  # Benutzer zur Eingabe des aktuellen Datenfelds auffordern
        daten = input()  # Benutzereingabe erfassen

        # Überprüfen, ob die Eingabe nicht leer ist
        if daten != "":
            daten_eingabe.append(daten)  # Eingabe zum aktuellen Datensatz hinzufügen
        else:
            print("darf nicht leer sein")  # Fehlermeldung, wenn die Eingabe leer ist
            break  # Die Schleife für die aktuelle Dateneingabe abbrechen, wenn die Eingabe leer ist

    # Überprüfen, ob Daten im aktuellen Datensatz vorhanden sind
    if daten_eingabe:
        gespeicherteDaten.append(daten_eingabe)  # Den aktuellen Datensatz speichern

    # Benutzer nach weiteren Dateneingaben fragen
    print("Wollen Sie weitere Daten eingeben?")
    print("j für Ja, n für Nein")
    eingabe = input()

    # Überprüfen, ob der Benutzer keine weiteren Dateneingaben wünscht
    if eingabe == "n":
        break

# Ausgabe aller gespeicherten Datensätze
for person in gespeicherteDaten:
    for (x, y) in zip(personenDaten, person):
        print(x, y)
    print()

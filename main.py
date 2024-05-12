import re
import pandas as pd

bezeichner_daten = ("Vorname", "Nachname", "Straße", "PLZ", "Ort")  # Tulpe da nicht veränderbar
UNGUELTIGE_EINGABE = "Ungültige Eingabe! Geben Sie folgendes ein! (ja/nein): \n"


def eingabe_daten():
    gespeicherte_daten = pd.DataFrame()  # DataFrame initialisieren
    # Schleife zur Dateneingabe
    while True:
        # Dictionary für jede einzelne Person erstellen
        personen_daten = {}

        for bezeichner in bezeichner_daten:
            while True:
                eingabe = input(f"Bitte geben Sie {bezeichner} ein: ")  # Benutzereingabe erfassen
                if eingabe.strip() == "":
                    print("Feld darf nicht leer sein")
                    continue
                break

            if not validierung(eingabe, bezeichner_daten.index(bezeichner)):
                print("Ungültige Eingabe")
                continue

            # Daten zum Dictionary hinzufügen
            personen_daten[bezeichner] = eingabe

        # Dictionary zum DataFrame hinzufügen
        gespeicherte_daten = pd.concat([gespeicherte_daten, pd.DataFrame([personen_daten])], ignore_index=True)

        # Abfrage zur weiteren Personenerfassung
        weitere_person = input("Möchten Sie weitere Personen erfassen? (ja/nein):\n")
        if weitere_person == "j":
            continue
        elif weitere_person == "n":
            abfrage(gespeicherte_daten)
        else:
            print(UNGUELTIGE_EINGABE)

    gespeicherte_daten.reset_index(drop=True, inplace=True)  # Index zurücksetzen
    return gespeicherte_daten


def ausgabe_daten(gespeicherte_daten):
    # Schleife zur Filterung
    while True:
        auswahl_filtern = input("Möchten Sie die Liste filtern? (ja/nein)):\n")
        if auswahl_filtern == "j":
            print("Verfügbare Bezeichner:")
            for i, bezeichner in enumerate(gespeicherte_daten.columns, 1):  # Index beginnt bei 1
                print(f"{i}. {bezeichner}")

            bezeichner_nr = int(input("Bitte geben Sie die Nummer des Bezeichners ein, "
                                      "nach dem Sie filtern möchten: ")) - 1  # -1 da Index normalerweise bei 0 beginnt
            bezeichner = gespeicherte_daten.columns[bezeichner_nr]
            filterkriterium = input(f"Bitte geben Sie das Filterkriterium für '{bezeichner}' ein: ")

            gefilterte_liste = gespeicherte_daten.query(f"{bezeichner} == '{filterkriterium}'")
            print("Gefilterte Daten:")
            print(gefilterte_liste)
        elif auswahl_filtern == "n":
            break
        else:
            print(UNGUELTIGE_EINGABE)

        # Abfrage zur Ausgabe der Daten
    while True:
        ausgabe_aufforderung = input("Möchten Sie die Daten ausgeben lassen? (ja/nein):\n")
        if ausgabe_aufforderung == "j":
            print("Gespeicherte Daten:\n" + gespeicherte_daten.to_string())  # String umwandeln
            exit()  # Programm wird geschlossen
        elif ausgabe_aufforderung == "n":
            print("Das Programm wird beendet!")
            exit()
        else:
            print(UNGUELTIGE_EINGABE)


def validierung(daten, bezeichner_index, ):
    validierungsregeln = {
        0: r'^[A-Za-zÄÖÜäöüß-]+$',  # Vorname
        1: r'^[A-Za-zÄÖÜäöüß-]+$',  # Nachname
        2: r'^[A-Za-zÄÖÜäöüß0-9\s.,/-]+$',  # Straße
        3: r'^\d{4}$',  # PLZ
        4: r'^[A-Za-zÄÖÜäöüß\s]+$',  # Ort
    }

    regel = validierungsregeln.get(bezeichner_index)  # Wert vom Dictionary überprüfen
    if not regel:
        return True

    if not re.match(regel, daten):
        print(f"Ungültige {bezeichner_daten[bezeichner_index]}.")
        return False
    return True


def filtern(gespeicherte_daten):
    while True:
        auswahl_filtern = input("Wollen Sie die Liste filtern? (ja/nein):\n")
        if auswahl_filtern == "j":
            print("Liste filtern")
        elif auswahl_filtern == "n":
            ausgabe_daten(gespeicherte_daten)
            break
        else:
            print(UNGUELTIGE_EINGABE)


def abfrage(gespeicherte_daten):
    while True:
        print("Was möchten Sie tun?\n1. Benutzer ändern\n2. Liste filtern\n3. Liste ausgeben\n")

        auswahl = input("Bitte geben Sie die Nummer der gewünschten Aktion ein: ")
        if auswahl == "1":
            benutzer_aendern(gespeicherte_daten)
            return True
        elif auswahl == "2":
            print("Liste filtern")
            return True
        elif auswahl == "3":
            print(gespeicherte_daten.to_string())  # DataFrame ausgeben
            exit()
        else:
            print(UNGUELTIGE_EINGABE)


def benutzer_aendern(gespeicherte_daten):
    # Liste der vorhandenen Benutzer anzeigen
    print("Liste der vorhandenen Benutzer:\n" + gespeicherte_daten.to_string(index=True))

    # ID des zu ändernden Benutzers abfragen
    id_zum_aendern = int(input("Bitte geben Sie die ID des zu ändernden Benutzers ein: ")) - 1
    if 0 <= id_zum_aendern < len(gespeicherte_daten):
        print(f"Ändern der Daten für Benutzer mit ID {id_zum_aendern + 1}:")
        gespeicherte_daten.at[id_zum_aendern] = eingabe_daten()
        print("Benutzer erfolgreich geändert.")
        abfrage(gespeicherte_daten)
    else:
        print("Ungültige ID.")


# Hier beginnt der Main-Teil
print("Herzlich Willkommen zur Datenerfassung.\nBitte geben Sie die Personendaten ein:\n")
eingabe_daten()

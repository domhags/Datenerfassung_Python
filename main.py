import re  # Modul re für reguläre Ausdrücke
import os  # Modul os für Dateiverarbeitung
import csv  # csv zum Speichern im csv Format

bezeichner_daten = ("Vorname", "Nachname", "Straße", "PLZ", "Ort")  # Tulpe da nicht veränderbar (Bezeichner)
UNGUELTIGE_EINGABE = "Ungültige Eingabe! Geben Sie folgendes ein! (ja/nein):\n"  # Fehlermeldung (Konstante)
DATEI = os.path.join(os.path.dirname(__file__), "personen_daten.txt")  # Konstante zur Datei im selben Verzeichnis


# Funktion zum Einlesen aus einer Txt-Datei
def einlesen():
    gespeicherte_daten = {}  # Leeres Dictionary erstellen
    try:
        with open(DATEI, "r", newline="") as file:  # Datei öffnen im Lese-Modus
            reader = csv.reader(file)
            next(reader)  # Überspringt die erste Zeile wegs den Bezeichnern
            for row in reader:
                person_id = len(gespeicherte_daten) + 1
                person = {bezeichner_daten[i]: value for i, value in enumerate(row)}
                gespeicherte_daten[person_id] = person  # Füge die Person dem Dictionary hinzu
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden oder konnte nicht geöffnet werden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    return gespeicherte_daten


# Funktion zum Schreiben in Datei und Speichern
def schreiben_und_speichern(gespeicherte_daten):
    with open(DATEI, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(bezeichner_daten)  # Bezeichner in der ersten Zeile
        for person in gespeicherte_daten.values():
            writer.writerow([person.get(key, "") for key in bezeichner_daten])


# Funktion zur Validierung der Eingaben
def validierung(daten, bezeichner_index):
    validierungsregeln = {
        0: r'^[A-Za-zÄÖÜäöüß-]+$',  # Vorname (r' = roher String)
        1: r'^[A-Za-zÄÖÜäöüß-]+$',  # Nachname (^ = Anfang des Strings)
        2: r'^[A-Za-zÄÖÜäöüß0-9\s.,/-]+$',  # Straße ([] = Zeichen die erlaubt sind und \s = Leerzeichen)
        3: r'^\d{4}$',  # PLZ (\d = 4 Ziffern folgend für Österreich)
        4: r'^[A-Za-zÄÖÜäöüß\s]+$',  # Ort (+ = Mindestens einmal vorkommen und $ = Ende vom String)
    }

    regel = validierungsregeln.get(bezeichner_index)  # Abrufen der Validierungsregel
    if regel and not re.match(regel, daten):  # Wenn keine Regel vorhanden ist
        bezeichner = bezeichner_daten[bezeichner_index]
        if bezeichner_index == 3:
            print(f"Ungültige Eingabe: {bezeichner}. Bitte geben Sie eine vierstellige Zahl ein.")
        else:
            print(f"Ungültige Eingabe für {bezeichner}. Bitte geben Sie nur Buchstaben ein.")
        return False
    return True


# Funktion zur Eingabe der Daten
def eingabe_daten(gespeicherte_daten=None):  # Zuerst None da bei jedem Aufruf Dictionary gelöscht wird
    if gespeicherte_daten is None:  # Wenn kein Dictionary vorhanden ist (Erstmaliges Aufrufen)
        gespeicherte_daten = {}  # Dictionary initialisieren
    person_id = len(gespeicherte_daten) + 1  # ID bei 1 beginnen (normal bei 0)

    # Schleife zur Dateneingabe
    while True:
        # Dictionary für jede einzelne Person erstellen
        personen_daten = {}
        for bezeichner in bezeichner_daten:
            while True:
                eingabe = input(f"Bitte geben Sie {bezeichner} ein: ")  # Benutzereingabe erfassen
                if eingabe.strip() == "":  # Eingabe darf nicht leer sein
                    print("Feld darf nicht leer sein")
                    continue
                if not validierung(eingabe, bezeichner_daten.index(bezeichner)):  # Überprüfen der Eingaben
                    continue
                break
            # Daten zum Dictionary hinzufügen
            personen_daten[bezeichner] = eingabe

        gespeicherte_daten[person_id] = personen_daten  # Speichert die Person mit der ID Nummer
        person_id += 1  # Erhöhen der ID

        if not weitere_personen():  # Abfrage für weitere Personeneingabe
            break

    ausgabe_daten(gespeicherte_daten)
    abfrage(gespeicherte_daten)
    return gespeicherte_daten


def weitere_personen():
    abfrage_weitere_personen = input("Möchten Sie weitere Personen erfassen? (ja/nein):\n")
    if abfrage_weitere_personen == "j":
        return True
    elif abfrage_weitere_personen == "n":
        return False
    else:
        print(UNGUELTIGE_EINGABE)


# Funktion zum Filtern der Daten
def filtern(gespeicherte_daten):
    gefilterte_liste = []

    print("Verfügbare Bezeichner:")
    # Schleife zur Filterung
    for i, bezeichner in enumerate(bezeichner_daten, 1):
        print(f"{i}. {bezeichner}")

    bezeichner_nr = int(input("Bitte geben Sie die Nummer des Bezeichners ein, nach dem Sie filtern möchten: "))
    bezeichner = bezeichner_daten[bezeichner_nr - 1]
    filterkriterium = input(f"Bitte geben Sie das Filterkriterium für '{bezeichner}' ein: ")

    for person in gespeicherte_daten.values():
        if person[bezeichner] == filterkriterium:
            gefilterte_liste.append(person)

    if gefilterte_liste:  # Überprüfen, ob die Liste nicht leer ist
        print("\nGefilterte Daten:")
        for person in gefilterte_liste:
            for bezeichner, daten in person.items():
                print(f"{bezeichner}: {daten}")
            print()
    else:
        print("Keine Daten gefunden, die dem Filterkriterium " + filterkriterium + " entsprechen.")


# Funktion zur Ausgabe der Daten
def ausgabe_daten(gespeicherte_daten):
    print("Gespeicherte Daten:\n")
    for person_id, person in gespeicherte_daten.items():
        print(f"Person {person_id}")
        for key, value in person.items():
            print(f"{key}: {value}")
        print()


# Funktion für weitere Aktionen im Programm
def abfrage(gespeicherte_daten):
    while True:
        print("Was möchten Sie tun?\n1. Benutzer ändern\n2. Liste filtern\n"
              "3. Benutzer hinzufügen\n4. Speichern\n5. Alle Datensätze anzeigen\n6. Programm beenden")

        auswahl = input("Bitte geben Sie die Nummer der gewünschten Aktion ein: ")
        if auswahl == "1":
            benutzer_aendern(gespeicherte_daten)
        elif auswahl == "2":
            filtern(gespeicherte_daten)
        elif auswahl == "3":
            eingabe_daten(gespeicherte_daten)
        elif auswahl == "4":
            schreiben_und_speichern(gespeicherte_daten)
            print("Datei gespeichert")
        elif auswahl == "5":
            ausgabe_daten(gespeicherte_daten)
        elif auswahl == "6":
            print("Programm wird beendet")
            break
        else:
            print(UNGUELTIGE_EINGABE)


# Funktion für Benutzeränderung
def benutzer_aendern(gespeicherte_daten):
    print("Liste der vorhandenen Benutzer:\n")

    for person_id, person in gespeicherte_daten.items():
        print(f"ID: {person_id}")

        for bezeichner, daten in person.items():
            print(f"{bezeichner}: {daten}")
        print()

    # ID abfragen
    id_zum_aendern = int(input("Bitte geben Sie die ID des zu ändernden Benutzers ein: "))
    # Überprüfen, ob ID vorhanden ist
    if id_zum_aendern in gespeicherte_daten:
        print(f"Ändern der Daten für Benutzer mit ID {id_zum_aendern}:")

        for bezeichner in bezeichner_daten:
            aktuelle_daten = gespeicherte_daten[id_zum_aendern][bezeichner]  # Anzeigen der "alten" Werte
            neue_daten = input(f"{bezeichner}: ({aktuelle_daten}) ")
            # Überprüfen, ob neue Daten eingegeben wurden
            if neue_daten.strip() == "":
                print("Eingabe darf nicht leer sein.")
            else:
                # Validierung der neuen Daten
                if validierung(neue_daten, bezeichner_daten.index(bezeichner)):
                    gespeicherte_daten[id_zum_aendern][bezeichner] = neue_daten
                else:
                    # Fehlermeldung bei ungültiger Eingabe und Beibehalten der alten Daten
                    print(f"Ungültige Eingabe für {bezeichner}. Behalten der alten Daten.")
        ausgabe_daten(gespeicherte_daten)
    else:
        print("Ungültige ID.")  # Fehlermeldung für ungültige Benutzer-ID


# Hier beginnt der Main-Teil
if __name__ == "__main__":
    alle_daten = einlesen()

    print("Herzlich Willkommen zur Datenerfassung.\n")
    abfrage(alle_daten)

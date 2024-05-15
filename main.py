import re  # Modul re für reguläre Ausdrücke

bezeichner_daten = ("Vorname", "Nachname", "Straße", "PLZ", "Ort")  # Tulpe da nicht veränderbar
UNGUELTIGE_EINGABE = "Ungültige Eingabe! Geben Sie folgendes ein! (ja/nein):\n"  # Fehlermeldung (Konstante)


# Funktion zur Validierung der Eingaben
def validierung(daten, bezeichner_index, ):
    validierungsregeln = {
        0: r'^[A-Za-zÄÖÜäöüß-]+$',  # Vorname (r' = roher String)
        1: r'^[A-Za-zÄÖÜäöüß-]+$',  # Nachname (^ = Anfang des Strings)
        2: r'^[A-Za-zÄÖÜäöüß0-9\s.,/-]+$',  # Straße ([] = Zeichen die erlaubt sind und \s = Leerzeichen)
        3: r'^\d{4}$',  # PLZ (\d = 4 Ziffern folgend für Österreich)
        4: r'^[A-Za-zÄÖÜäöüß\s]+$',  # Ort (+ = Mindestens einmal vorkommen und $ = Ende vom String)
    }

    regel = validierungsregeln.get(bezeichner_index)  # Abrufen der Validierungsregel
    if regel and not re.match(regel, daten):  # Wenn keine Regel vorhanden ist
        print(f"Ungültige Eingabe: {bezeichner_daten[bezeichner_index]}")
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

    if gefilterte_liste:  # Überprüfen ob die Liste nicht leer ist
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
        print("Was möchten Sie tun?\n1. Benutzer ändern\n2. Liste filtern\n3. Benutzer hinzufügen\n")

        auswahl = input("Bitte geben Sie die Nummer der gewünschten Aktion ein: ")
        if auswahl == "1":
            benutzer_aendern(gespeicherte_daten)
        elif auswahl == "2":
            filtern(gespeicherte_daten)
        elif auswahl == "3":
            eingabe_daten(gespeicherte_daten)
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
    print("Herzlich Willkommen zur Datenerfassung.\nBitte geben Sie die Personendaten ein:\n")
    eingabe_daten()

import re

gespeicherteDaten = []


def eingabe_daten():
    bezeichnerDaten = ["Vorname: ", "Nachname: ", "Straße: ", "PLZ: ", "Ort: "]  # Liste der Datenfelder

    # Hauptschleife zur Dateneingabe
    while True:
        personenListe = []
        for i, person in enumerate(bezeichnerDaten):  # enumerate ließt den Index mit
            while True:
                daten = input(person)  # Benutzereingabe erfassen
                if daten.strip() == "":
                    print("Feld darf nicht leer sein")
                elif validierung(daten, i):
                    personenListe.append(daten)
                    break
                else:
                    print("Ungültige Eingabe")

            gespeicherteDaten.append(personenListe.copy())  # Eine Kopie von personenListe wird hinzugefügt
            personenListe.clear()  # personenListe wird gelöscht.

        weitere_daten()


def ausgabe_daten():
    # Abfrage zur Ausgabe der Daten
    while True:
        auswahl = input("Möchten Sie die Daten ausgeben lassen?\nj für Ja, n für Nein\n")
        if auswahl == "j":
            print(f"{gespeicherteDaten}")
            return True
        elif auswahl == "n":
            print("Das Programm wird beendet!")
            exit()
        else:
            print("Ungültige Eingabe. Bitte geben Sie j für j, n für Nein ein!")


def validierung(daten, index):
    if index == 0 and not re.match(r'^[A-Za-zÄÖÜäöüß-]+$', daten):
        print("Ungültiger Vorname. Bitte verwenden Sie nur Buchstaben und Bindestriche.")
        return False
    elif index == 1 and not re.match(r'^[A-Za-zÄÖÜäöüß-]+$', daten):
        print("Ungültiger Nachname. Bitte verwenden Sie nur Buchstaben und Bindestriche.")
        return False
    elif index == 2 and not re.match(r'^[A-Za-zÄÖÜäöüß0-9\s.,/-]+$', daten):
        print("Ungültige Straße. Bitte verwenden Sie nur Buchstaben, Zahlen und Sonderzeichen.")
        return False
    elif index == 3 and not re.match(r'^\d{4}$', daten):
        print("Ungültige PLZ. Bitte geben Sie eine 4-stellige Zahl für Österreich ein.")
        return False
    elif index == 4 and not re.match(r'^[A-Za-zÄÖÜäöüß\s]+$', daten):
        print("Ungültiger Ort. Bitte verwenden Sie nur Buchstaben.")
        return False
    return True


def weitere_daten():
    while True:
        eingabe = input("Wollen Sie weitere Daten eingeben?\nj für Ja, n für Nein\n")

        if eingabe == "j":
            eingabe_daten()
        elif eingabe == "n":
            ausgabe_daten()
        else:
            print("Falsche Eingabe! Geben Sie j für ja oder n für nein ein\n")


# Hier beginnt der Main-Teil
print("Herzlich Willkommen zur Datenerfassung.\nBitte geben Sie die Personendaten ein:\n")
eingabe_daten()

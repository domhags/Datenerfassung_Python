from funktionen import *  # Importiert alle Funktionen aus der Datei 'funktionen'
import tkinter as tk  # Importiert das Tkinter-Modul für die GUI-Erstellung
from tkinter import ttk  # Importiert das ttk-Modul für erweiterte Tkinter-Widgets


# Funktion zum Erstellen der GUI
def erstelle_gui():
    # Erstellt das Hauptfenster der Anwendung
    root = tk.Tk()
    root.title("Personenerfassung")  # Setzt den Titel des Fensters

    # Erstellt das Treeview-Widget mit den definierten Spaltenbezeichnungen
    tree = ttk.Treeview(root, columns=BEZEICHNUNGEN, show="headings")
    for bezeichnung in BEZEICHNUNGEN:
        tree.heading(bezeichnung, text=bezeichnung)  # Setzt die Überschriften der Spalten
    tree.pack(pady=20)  # Platziert das Treeview im Haupt-Frame

    # Erstellt einen Frame für die Eingabefelder
    eingabe_frame = tk.Frame(root)
    eingabe_frame.pack(pady=10)  # Platziert den Frame im Fenster

    eingaben = [tk.Entry(eingabe_frame) for _ in BEZEICHNUNGEN]
    for idx, (bezeichnung, eingabe) in enumerate(zip(BEZEICHNUNGEN, eingaben)):
        tk.Label(eingabe_frame, text=f"{bezeichnung}:").grid(row=0, column=idx)
        eingabe.grid(row=1, column=idx)

    # # Bindet die Enter-Taste an die Funktion zum Hinzufügen eines Eintrags
    # eingabe_frame.bind("<Return>", lambda event: eintrag_hinzufuegen_enter(tree, *eingabe_liste))
    # eingabe_frame.focus_set()

    # Erstellt den Hinzufügen-Button und bindet die entsprechende Funktion
    hinzufuegen_button = tk.Button(root, text="Hinzufügen",
                                   command=lambda: eintrag_hinzufuegen(tree, *eingaben))
    hinzufuegen_button.pack(pady=10)  # Platziert den Button im Frame (east, west)

    # Erstellt den Liste Löschen-Button und bindet die entsprechende Funktion
    loeschen_button = tk.Button(root, text="Liste löschen", command=lambda: liste_loeschen(tree))
    loeschen_button.pack(pady=10)  # Platziert den Button im Frame

    # Erstellt den Speichern-Button und bindet die entsprechende Funktion
    speichern_button = tk.Button(root, text="Liste in Datei speichern",
                                 command=lambda: in_datei_speichern(liste_ausgeben(tree)))
    speichern_button.pack(pady=10)  # Platziert den Button im Frame

    # Erstellt den Einlesen-Button und bindet die entsprechende Funktion
    einlesen_button = tk.Button(root, text="Liste aus Datei einlesen",
                                command=lambda: aus_datei_einlesen(tree))
    einlesen_button.pack(pady=10)  # Platziert den Button im Frame

    # Erstellt den Bearbeiten-Button und bindet die entsprechende Funktion
    bearbeiten_button = tk.Button(root, text="Eintrag bearbeiten",
                                  command=lambda: eintrag_bearbeiten(tree, root))
    bearbeiten_button.pack(pady=10)  # Platziert den Button im Frame

    # Erstellt den Benutzer Löschen-Button und bindet die entsprechende Funktion
    benutzer_loeschen_button = tk.Button(root, text="Benutzer löschen", command=lambda: benutzer_loeschen(tree))
    benutzer_loeschen_button.pack(pady=10)  # Platziert den Button im Frame

    # Erstellt den Beenden-Button, um die Anwendung zu schließen
    beenden_button = tk.Button(root, text="Beenden", command=root.quit)
    beenden_button.pack(pady=10)  # Platziert den Button im Frame

    # Startet die Haupt-Event-Loop der Anwendung, damit die GUI angezeigt wird
    root.mainloop()


# Hier beginnt der Main-Teil der Anwendung
if __name__ == "__main__":
    erstelle_gui()  # Ruft die Funktion auf, um die GUI zu erstellen und zu starten

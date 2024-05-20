from funktionen import *  # Importiert alle Funktionen aus der Datei 'funktionen'
import tkinter as tk  # Importiert das Tkinter-Modul für die GUI-Erstellung
from tkinter import ttk  # Importiert das ttk-Modul für erweiterte Tkinter-Widgets


# Funktion zum Erstellen der GUI
def erstelle_gui():
    # Erstellt das Hauptfenster der Anwendung
    root = tk.Tk()
    root.title("Personenerfassung")  # Setzt den Titel des Fensters

    # Erstellt einen Haupt-Frame, der das Treeview-Widget enthält
    haupt_frame = tk.Frame(root)
    haupt_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)  # Platziert den Frame im Fenster

    # Erstellt das Treeview-Widget mit den definierten Spaltenbezeichnungen
    tree = ttk.Treeview(haupt_frame, columns=BEZEICHNUNGEN, show="headings")
    for bezeichnung in BEZEICHNUNGEN:
        tree.heading(bezeichnung, text=bezeichnung, anchor="w")  # Setzt die Überschriften der Spalten
    tree.pack()  # Platziert das Treeview im Haupt-Frame

    # Erstellt einen Frame für die Eingabefelder
    eingabe_frame = tk.Frame(root)
    eingabe_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)  # Platziert den Frame im Fenster

    label_liste = []  # Liste zum Speichern der Label-Widgets
    eingabe_liste = []  # Liste zum Speichern der Eingabefeld-Widgets

    # Erstellt die Eingabefelder und Labels dynamisch basierend auf den Bezeichnungen
    for idx, bezeichnung in enumerate(BEZEICHNUNGEN):
        label = tk.Label(eingabe_frame, text=bezeichnung, anchor="w")  # Erstellt ein Label
        label.grid(row=0, column=idx, padx=5, pady=5, sticky="ew")  # Platziert das Label im Grid-Layout

        eingabe = tk.Entry(eingabe_frame)  # Erstellt ein Eingabefeld
        eingabe.grid(row=1, column=idx, padx=5, pady=5, sticky="ew")  # Platziert das Eingabefeld im Grid-Layout
        # Bindet das Label an eine Markierungsfunktion (kann später angepasst werden)
        label.bind("<Button-1>", lambda event, entry=eingabe: markieren_vn(eingabe))
        label_liste.append(label)  # Fügt das Label der Liste hinzu
        eingabe_liste.append(eingabe)  # Fügt das Eingabefeld der Liste hinzu

    # Bindet die Enter-Taste an die Funktion zum Hinzufügen eines Eintrags
    eingabe_frame.bind("<Return>", lambda event: eintrag_hinzufuegen_enter(tree, *eingabe_liste))

    # Erstellt einen Frame für die Buttons
    button_frame = tk.Frame(root)
    button_frame.pack(padx=10, pady=10)  # Platziert den Frame im Fenster

    # Konfiguriert 2 Spalten für das Grid-Layout der Buttons
    button_frame.columnconfigure(0)
    button_frame.columnconfigure(1)

    # Erstellt den Hinzufügen-Button und bindet die entsprechende Funktion
    hinzufuegen_button = tk.Button(button_frame, text="Hinzufügen",
                                   command=lambda: eintrag_hinzufuegen(tree, *eingabe_liste))
    hinzufuegen_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")  # Platziert den Button im Frame

    # Erstellt den Liste Löschen-Button und bindet die entsprechende Funktion
    loeschen_button = tk.Button(button_frame, text="Liste löschen", command=lambda: liste_loeschen(tree))
    loeschen_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")  # Platziert den Button im Frame

    # Erstellt den Speichern-Button und bindet die entsprechende Funktion
    speichern_button = tk.Button(button_frame, text="Liste in Datei speichern",
                                 command=lambda: in_datei_speichern(liste_ausgeben(tree)))
    speichern_button.grid(padx=10, pady=5)  # Platziert den Button im Frame

    # Erstellt den Einlesen-Button und bindet die entsprechende Funktion
    einlesen_button = tk.Button(button_frame, text="Liste aus Datei einlesen",
                                command=lambda: aus_datei_einlesen(tree))
    einlesen_button.grid(row=1, column=1, padx=10, pady=5, sticky="ew")  # Platziert den Button im Frame

    # Erstellt den Bearbeiten-Button und bindet die entsprechende Funktion
    bearbeiten_button = tk.Button(button_frame, text="Eintrag bearbeiten",
                                  command=lambda: eintrag_bearbeiten(tree, root))
    bearbeiten_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")  # Platziert den Button im Frame

    # Erstellt den Beenden-Button, um die Anwendung zu schließen
    beenden_button = tk.Button(button_frame, text="Beenden", command=root.quit)
    beenden_button.grid(row=2, column=1, padx=10, pady=5, sticky="ew")  # Platziert den Button im Frame

    # Startet die Haupt-Event-Loop der Anwendung, damit die GUI angezeigt wird
    root.mainloop()


# Hier beginnt der Main-Teil der Anwendung
if __name__ == "__main__":
    erstelle_gui()  # Ruft die Funktion auf, um die GUI zu erstellen und zu starten

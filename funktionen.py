import tkinter as tk  # Importiert das Tkinter-Modul für die GUI-Erstellung
from tkinter import messagebox  # Importiert das Messagebox
import os  # Importiert das os-Modul zur Arbeit mit Dateipfaden

# Name der Datei, in der die Personendaten gespeichert werden
DATEI_NAME = "personen_daten.txt"

# Bezeichnungen der Spalten
BEZEICHNUNGEN = ["Vorname", "Nachname", "Straße", "PLZ", "Ort"]


# Funktion zum Erstellen des vollständigen Dateipfads
def datei_pfad_erstellen():
    return os.path.join(os.getcwd(), DATEI_NAME)  # Gibt den vollständigen Pfad zur Datei zurück


# # Funktion zum Hinzufügen von Einträgen bei Drücken der Enter-Taste
# def eintrag_hinzufuegen_enter(tree, *eingaben):
#     werte = sammle_eingabewerte(*eingaben)  # Sammelt die Werte aus den Eingabefeldern
#     tree.insert("", "end", values=werte) # Fügt die Werte als neuen Eintrag in das Treeview ein
#     loesche_eingaben(*eingaben)  # Löscht die Eingabefelder


# Funktion zum Löschen von Einträgen in den Eingabefeldern
def loesche_eingaben(*eingaben):
    for eingabe in eingaben:
        eingabe.delete(0, tk.END)  # Löscht den Text in jedem Eingabefeld


# Funktion zum Ausgeben der Liste aus dem Treeview
def liste_ausgeben(tree):
    # Gibt die Werte aller Einträge im Treeview zurück
    return [tree.item(element)["values"] for element in tree.get_children()]  # List-Comprehension über alle Elemente


# Funktion zum Speichern der Liste in eine Datei
def in_datei_speichern(liste):
    datei_pfad = datei_pfad_erstellen()  # Erstellt den Dateipfad
    try:
        with open(datei_pfad, "w") as datei:
            for eintrag in liste:
                string_eintrag = [str(element) for element in eintrag]  # Konvertiert alle Elemente in Strings
                datei.write(";".join(string_eintrag) + "\n")  # Schreibt die Einträge in die Datei
    except IOError as e:
        # Zeigt eine Fehlermeldung an
        tk.messagebox.showerror("Fehler beim Speichern", f"Fehler beim Speichern der Datei: {e}")


# Funktion zum Einlesen der Liste aus einer Datei
def aus_datei_einlesen(tree):
    datei_pfad = datei_pfad_erstellen()  # Erstellt den Dateipfad
    try:
        with open(datei_pfad, "r") as datei:
            for zeile in datei:
                werte = zeile.strip().split(";")  # Trennt die Zeile in einzelne Werte
                tree.insert("", "end", values=werte)  # Fügt die Werte als neuen Eintrag in das Treeview ein
            letzte_reihe_fokussieren(tree)  # Fokussiert die letzte Reihe im Treeview
    except IOError as e:
        # Zeigt eine Fehlermeldung an
        tk.messagebox.showerror("Fehler beim Lesen", f"Fehler beim Lesen der Datei: {e}")


# Funktion zum Markieren des Texts in einem Eingabefeld (bei Event)
def markieren_vn(eingabe):
    eingabe.select_range(0, "end")  # Markiert den gesamten Text im Eingabefeld


# Funktion zum Hinzufügen eines Eintrags
def eintrag_hinzufuegen(tree, *eingaben):
    werte = sammle_eingabewerte(*eingaben)  # Sammelt die Werte aus den Eingabefeldern
    if not all(werte):
        tk.messagebox.showerror("Fehler", "Bitte füllen Sie alle Felder aus.")
        return
    tree.insert("", "end", values=werte)  # Fügt die Werte als neuen Eintrag in das Treeview ein
    loesche_eingaben(*eingaben)  # Löscht die Eingabefelder
    letzte_reihe_fokussieren(tree)  # Fokussiert die letzte Reihe im Treeview


# Funktion zum Fokussieren der letzten Reihe im Treeview
def letzte_reihe_fokussieren(tree):
    letzter_eintrag = tree.get_children()[-1]  # Holt den letzten Eintrag im Treeview
    tree.selection_set(letzter_eintrag)  # Markiert den letzten Eintrag
    tree.focus(letzter_eintrag)  # Setzt den Fokus auf den letzten Eintrag
    tree.see(letzter_eintrag)  # Scrollt zum letzten Eintrag


# Funktion zum Löschen aller Einträge im Treeview
def liste_loeschen(tree):
    tree.delete(*tree.get_children())  # Löscht alle Einträge im Treeview


# Funktion zum Bearbeiten eines Eintrags
def eintrag_bearbeiten(tree, root):
    ausgewaehlte_eintraege = tree.selection()  # Holt die ausgewählten Einträge im Treeview
    if ausgewaehlte_eintraege:
        werte = tree.item(ausgewaehlte_eintraege[0])["values"]  # Holt die Werte des ersten ausgewählten Eintrags
        bearbeiten_fenster = tk.Toplevel(root)  # Erstellt ein neues Fenster für die Bearbeitung
        bearbeiten_fenster.title("Benutzer bearbeiten")  # Setzt den Titel des Fensters
        bearbeiten_fenster.geometry("300x200")  # Setzt die Größe des Fensters
        eingaben = []

        for idx, (bezeichnung, wert) in enumerate(zip(BEZEICHNUNGEN, werte)):
            tk.Label(bearbeiten_fenster, text=f"{bezeichnung}:").grid(row=idx, column=0)  # Erstellt ein Label
            eingabe = tk.Entry(bearbeiten_fenster)  # Erstellt ein Eingabefeld
            eingabe.grid(row=idx, column=1)  # Platziert das Eingabefeld
            eingabe.insert(0, wert)  # Fügt den bestehenden Wert in das Eingabefeld ein
            eingaben.append(eingabe)  # Fügt das Eingabefeld der Liste hinzu

        # Erstellt den Button zum Speichern der Änderungen
        speichern_button = tk.Button(
            bearbeiten_fenster,
            text="Änderungen speichern",
            command=lambda: aenderungen_speichern(tree, ausgewaehlte_eintraege, eingaben, bearbeiten_fenster))
        speichern_button.grid(row=len(werte), columnspan=2)  # Platziert den Button
    else:
        tk.messagebox.showerror("Fehler", "Es wurde kein Eintrag zum Bearbeiten ausgewählt")


# Funktion zum Speichern der Änderungen
def aenderungen_speichern(tree, ausgewaehlte_eintraege, eingaben, fenster):
    neue_werte = [eingabe.get() for eingabe in eingaben]  # Holt die neuen Werte aus den Eingabefeldern
    if not all(neue_werte):
        tk.messagebox.showerror("Fehler", "Bitte füllen Sie alle Felder aus.")
        return
    tree.item(ausgewaehlte_eintraege[0], values=neue_werte)  # Aktualisiert den Eintrag im Treeview
    fenster.destroy()  # Schließt das Bearbeitungsfenster


# Funktion zum Sammeln der Werte der Eingabefelder
def sammle_eingabewerte(*eingaben):
    return [eingabe.get() for eingabe in eingaben]  # Gibt die Werte der Eingabefelder als Liste zurück


# Funktion für einen Benutzer gezielt löschen
def benutzer_loeschen(tree):
    # Überprüfen, ob ein Eintrag im Treeview markiert ist
    selected_item = tree.focus()
    if selected_item:
        tree.delete(selected_item)  # Löscht den markierten Eintrag im Treeview
    else:
        messagebox.showerror("Fehler", "Es wurde kein Eintrag zum Löschen ausgewählt.")

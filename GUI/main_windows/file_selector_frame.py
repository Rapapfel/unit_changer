import customtkinter as ctk
from tkinter import filedialog

class file_selector_frame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Unit Changer")
        self.geometry("650x365")

        self.widgets_erstellen()

    def widgets_erstellen(self):
        # Beschriftung
        self.beschriftung = ctk.CTkLabel(self, text="Bitte wählen Sie den Dateipfad der IFC-Datei, bei der Sie die Einheiten ändern möchten")
        self.beschriftung.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
        
        # Schaltfläche, um abzubrechen und die Anwendung zu schließen (Links)
        self.abbrechen_schaltflaeche = ctk.CTkButton(self, text="Abbrechen", command=self.anwendung_schliessen)
        self.abbrechen_schaltflaeche.place(relx=0.2, rely=0.6, anchor=ctk.CENTER)
        
        # Schaltfläche, um den Dateipfad auszuwählen (Mitte)
        self.waehlen_schaltflaeche = ctk.CTkButton(self, text="Wählen", command=self.datei_auswaehlen)
        self.waehlen_schaltflaeche.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)
        
        # Schaltfläche, um zum nächsten Schritt fortzufahren (Rechts)
        self.weiter_schaltflaeche = ctk.CTkButton(self, text="Weiter", command=self.weiter_aktion)
        self.weiter_schaltflaeche.place(relx=0.8, rely=0.6, anchor=ctk.CENTER)

        # Eingabefeld für den Dateipfad, für Benutzereingaben deaktiviert
        self.dateipfad_eingabe = ctk.CTkEntry(self, width=600, state='disabled', placeholder_text="VAR_DATEIPFAD")
        self.dateipfad_eingabe.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

    def datei_auswaehlen(self):
        # Einen Datei-Dialog öffnen, um eine Datei auszuwählen und den Pfad im Eingabefeld anzeigen
        dateipfad = filedialog.askopenfilename()
        if dateipfad:
            self.dateipfad_eingabe.configure(state='normal')  # Aktiviert das Eingabefeld, um den Text zu ändern
            self.dateipfad_eingabe.delete(0, ctk.END)
            self.dateipfad_eingabe.insert(0, dateipfad)
            self.dateipfad_eingabe.configure(state='disabled')  # Deaktiviert das Eingabefeld wieder

    def weiter_aktion(self):
        # Platzhalter für die Aktion, die ausgeführt werden soll, wenn 'Weiter' geklickt wird
        pass

    def anwendung_schliessen(self):
        # Die Anwendung schließen
        self.destroy()

if __name__ == "__main__":
    app = file_selector_frame()
    app.mainloop()
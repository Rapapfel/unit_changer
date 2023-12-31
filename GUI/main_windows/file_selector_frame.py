import customtkinter as ctk
from tkinter import filedialog

class file_selector_frame(ctk.CTkFrame):
    def __init__(self, container, X, Y):
        """
        Konstruktor für die FileSelectorFrame-Klasse.
        
        Args:
            container: Das übergeordnete Container-Objekt.
            X: Die Breite des Frames.
            Y: Die Höhe des Frames.
        """
        self.fg_color = "#242424"
        super().__init__(container, width=X, height=Y, fg_color=self.fg_color)
        self.selected_file_path = None  # Initialisieren Sie die Variable mit None
        self.container = container

        self.widgets_erstellen()

    def widgets_erstellen(self):
        """
        Methode zur Erstellung der GUI-Widgets im Frame.
        """
        # Beschriftung
        self.beschriftung = ctk.CTkLabel(self, text="Bitte wählen Sie den Dateipfad der IFC-Datei, bei der Sie die Einheiten ändern möchten")
        self.beschriftung.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
        
        # Schaltfläche, um abzubrechen und die Anwendung zu schließen (Links)
        self.abbrechen_schaltflaeche = ctk.CTkButton(self, text="Abbrechen", command=self.anwendung_schliessen)
        self.abbrechen_schaltflaeche.place(relx=0.3, rely=0.6, anchor=ctk.CENTER)
        
        # Schaltfläche, um den Dateipfad auszuwählen (Mitte)
        self.waehlen_schaltflaeche = ctk.CTkButton(self, text="Wählen", command=self.datei_auswaehlen)
        self.waehlen_schaltflaeche.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)
        
        # Schaltfläche, um zum nächsten Schritt fortzufahren (Rechts)
        self.weiter_schaltflaeche = ctk.CTkButton(self, text="Weiter", command=self.weiter_aktion)
        self.weiter_schaltflaeche.place(relx=0.7, rely=0.6, anchor=ctk.CENTER)

        # Eingabefeld für den Dateipfad, für Benutzereingaben deaktiviert
        self.dateipfad_eingabe = ctk.CTkEntry(self, width=900, state='disabled', placeholder_text="VAR_DATEIPFAD", justify= "center")
        self.dateipfad_eingabe.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

    def datei_auswaehlen(self):
        """
        Methode zum Auswählen des Dateipfads über einen Datei-Dialog.
        """
        # Einen Datei-Dialog öffnen, um eine Datei mit der Erweiterung ".ifc" auszuwählen und den Pfad im Eingabefeld anzeigen
        filetypes = [("IFC-Dateien", "*.ifc")]
        dateipfad = filedialog.askopenfilename(filetypes=filetypes)
        if dateipfad:
            self.selected_file_path = dateipfad  # Speichern des Pfades als Attribut der Klasse
            self.dateipfad_eingabe.configure(state='normal')  # Aktiviert das Eingabefeld, um den Text zu ändern
            self.dateipfad_eingabe.delete(0, ctk.END)
            self.dateipfad_eingabe.insert(0, dateipfad)
            self.dateipfad_eingabe.configure(state='disabled')  # Deaktiviert das Eingabefeld wieder

    def weiter_aktion(self):
        """
        Methode zur Fortsetzung der Anwendung nach Auswahl der Datei.
        """
        if self.selected_file_path:
            self.container.ifc_import_callback(self.selected_file_path)

    def anwendung_schliessen(self):
        """
        Methode zum Schließen der Anwendung.
        """
        # Die Anwendung schließen
        self.container.abbrechen()

if __name__ == "__main__":
    # Erstellen des Hauptfensters
    root = ctk.CTk()

    # Konfiguration der Fenstergröße und Position
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = (3 * screen_width) // 4
    window_height = (2 * screen_height) // 3
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Instanziieren und Anzeigen des Frames
    frame = file_selector_frame(root, window_width - 60, window_height)
    frame.pack(fill="both", expand=True)

    # Starten des Event-Loops
    root.mainloop()

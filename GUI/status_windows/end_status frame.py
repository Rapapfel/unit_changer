import customtkinter as ctk

class end_status_frame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Fertig")
        self.geometry("450x200")
        self.attributes("-topmost",True)

        self.widgets_erstellen()

    def widgets_erstellen(self):
        # Beschriftung für die Feritginformation
        text1 = "Die Einheiten der gewählten IFC-Datei wurden umgewandelt und"
        text2 = "eine neue IFC-Datei unter ihrem angegebenen Pfad abgespeichert"

        label1 = ctk.CTkLabel(self, text=text1)
        label1.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)

        label2 = ctk.CTkLabel(self, text=text2)
        label2.place(relx=0.5, rely=0.46, anchor=ctk.CENTER)

        # Beenden-Schaltfläche zum Schließen des Fensters und Programms
        self.end_button = ctk.CTkButton(self, text="Beenden", command=self.fenster_schliessen)
        self.end_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

    def fenster_schliessen(self):
        self.destroy()

if __name__ == "__main__":
    app = end_status_frame()
    app.mainloop()
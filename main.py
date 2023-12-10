import customtkinter as ctk
from GUI.main_windows.file_selector_frame import file_selector_frame as fsf
from IFC_operation.file_reader import modules_ifc_operation as modules # Check if IFC is corrupted
from GUI.status_windows.file_selector_status_frame import file_selctor_status_frame as fssf # File unsuccessfully imported
from GUI.status_windows.unit_status_frame import unit_status_frame as usf # File successfully imported
from GUI.main_windows.unit_selector_frame import Unit_selector
from GUI.template_windows.template_frame import BenutzerdefinierteVorlagen as bv

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Unit Changer")
        self.geometry("2000x1000")
        self.current_frame = None

        self.fsf = fsf(self)
        self.frame_selection(self.fsf)
        print("finish")

    def frame_selection(self, frame):
        if self.current_frame != None:
            self.current_frame.place_forget()
        
        frame.place(relx=0.5, rely=0.5, anchor="center")
        self.current_frame = frame
    
    # Callback-Funktion für IFC-Import
    def ifc_import_callback(self, filepath):
        if modules.is_ifc_file(filepath):
            # Öffnet das Statusfenster für erfolgreichen Import
            window_unit_status = usf(self, "SI")  # Ersetzen mit der effektiven Variable
            window_unit_status.mainloop()
            print("System Message:\tFile imported")
            self.frame_selection(Unit_selector(self))
            return True
        else:
            # Öffnet das Statusfenster für fehlgeschlagenen Import
            window_import_status = fssf()
            window_import_status.mainloop()
            print("System Message:\tError Message")
            return False
    
    def get_selected_file_path(self):
        return self.fsf.selected_file_path

    def unit_selector_callback(self):
        print("dugasd")
        self.frame_selection(bv(self))

    def abbrechen(self):
        self.destroy()
        




if __name__ == "__main__":
    app = Window()
    app.mainloop()

    selected_path = app.get_selected_file_path()

    selected_path = app.get_selected_file_path()

    # Wenn ein Dateipfad vorhanden ist, rufen Sie die extract_pset_parameters-Funktion auf
    if selected_path:
        pset_dict = modules.extract_pset_parameters(selected_path)
        
        # Drucken Sie das resultierende sorted_pset_dict
        print("Sorted Pset Dictionary:")
        print(pset_dict)



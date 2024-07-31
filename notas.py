import tkinter as tk
from utils import (
    create_header,
    create_label,
    create_submit_button,
    FieldFactory,
)

class NotesApp():
    def __init__(self, root) -> None:
        self.root = root
        self.root.config(background="white")
        self.root.title("Notas")
        
        self.form_frame = tk.Frame(self.root, background="white")
        self.result_frame = tk.Frame(self.root, background="white")
        
        create_header(self.root, "Calculadora de Notas IUPSM")
        self.note_1_field = FieldFactory(self.form_frame, "Ingrese la primera nota:")
        self.note_2_field = FieldFactory(self.form_frame, "Ingrese la segunda nota:")
        
        create_submit_button(self.form_frame, self.submit)
        
        self.form_frame.pack(padx=10, pady=10)
        
        self.final_note = create_label(self.result_frame, "Notas final: 0")
        self.obs = create_label(self.result_frame, "Observacion: ninguna")
        self.result_frame.pack(padx=10, pady=10)
        
    def submit(self):
        note_1 = float(self.note_1_field.input_entry.get())
        note_2 = float(self.note_2_field.input_entry.get())
        
        final_note = (note_1 + note_2) / 2
        
        self.final_note.config(text=f"Notas final: {final_note}")
        self.obs.config(text=self.makeObservation(final_note))
        
        self.note_1_field.input_entry.delete(0, tk.END)
        self.note_2_field.input_entry.delete(0, tk.END)
       
    
    def makeObservation(self,note: float) -> str: 
        if note < 10:
            return "Observacion: Debe estudiar Mas"
        
        return "Observacion: Va por buen Camino"


root = tk.Tk()
NotesApp(root)
root.mainloop()
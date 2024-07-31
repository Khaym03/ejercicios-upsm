import tkinter as tk
from utils import (
    spacing,
    create_header,
    create_submit_button,
    create_label,
    FieldFactory,
    RadioGroup,
    calc_avr_age_per_gender,
    Person
)


class PartyApp:
    numOfPersons = []

    def __init__(self, root):

        self.root = root
        self.root.config(background="white")
        self.root.title("Party")

        self.form_frame = tk.Frame(self.root, background="white")
        self.stats_frame = tk.Frame(self.root, background="white")

        create_header(root, "Bienvenido a la fiesta")
        self.age_field = FieldFactory(self.form_frame, "Ingrese su edad:")
        self.selected_gender = RadioGroup(
            self.form_frame, "Seleccione su género:", ["Femenino", "Masculino"]
        )

        create_submit_button(self.form_frame, self.submit)
        self.form_frame.pack(padx=10, pady=10)

        self.create_stats_frame()
        self.stats_frame.pack(padx=10, pady=10)

    def create_stats_frame(self):
        self.stats_label = tk.Label(
            self.stats_frame,
            text="Estadísticas de la Fiesta",
            font=("Arial", spacing.base, "bold"),
            background="white",
            justify="left",
        )
        self.stats_label.pack(anchor="w", pady=spacing.gap_1)

        self.total_label = create_label(
            self.stats_frame, "Total de personas: 0", spacing.sm
        )

        self.female_label = create_label(self.stats_frame, "Mujeres: 0", spacing.sm)

        self.male_label = create_label(self.stats_frame, "Hombres: 0", spacing.sm)

        self.oldest_label = create_label(
            self.stats_frame, "Persona más vieja: N/A", spacing.sm
        )

        self.avr_age_male = create_label(
            self.stats_frame, "Edad promedio de los hombres: N/A", spacing.sm
        )

        self.avr_age_female = create_label(
            self.stats_frame, "Edad promedio de las mujeres: N/A", spacing.sm
        )

    def submit(self):
        age = int(self.age_field.input_entry.get())
        gender = self.selected_gender.radio_var.get()

        self.numOfPersons.append(Person(age, gender))
        self.age_field.input_entry.delete(0, tk.END)

        self.update_stats()

    def update_stats(self):
        total = len(self.numOfPersons)
        
        female_count = sum(1 for person in self.numOfPersons if person.gender == "Femenino")
        male_count = sum(1 for person in self.numOfPersons if person.gender == "Masculino")

        oldest_age = max((person.age for person in self.numOfPersons), default="N/A")

        avr_female_age, avr_male_age = calc_avr_age_per_gender(self.numOfPersons)

        self.total_label.config(text=f"Total de personas: {total}")
        self.female_label.config(text=f"Mujeres: {female_count}")
        self.male_label.config(text=f"Hombres: {male_count}")
        self.oldest_label.config(text=f"Persona más vieja: {oldest_age} años")
        self.avr_age_male.config(text=f"Edad promedio de los hombres: {avr_male_age}")
        self.avr_age_female.config(
            text=f"Edad promedio de las mujeres: {avr_female_age}"
        )


root = tk.Tk()
app = PartyApp(root)
root.mainloop()

import tkinter as tk
from utils import (
    spacing,
    create_header,
    create_label,
    create_submit_button,
    FieldFactory,
    RadioGroup,
    calc_avr_age_per_gender,
    calc_avr_age,
    Person,
)


class TeamManager:
    leones = []
    navegantes = []
    tigres = []

    def addPerson(self, person, team):
        if team == "Leones":
            self.leones.append(person)

        if team == "Navegantes":
            self.navegantes.append(person)

        if team == "Tigres":
            self.tigres.append(person)

    def get_all_persons(self):
        return self.leones + self.navegantes + self.tigres


class FanaticApp:
    teams = ["Leones", "Navegantes", "Tigres"]
    leones, navegantes, tigres = teams

    fanatics = []

    def __init__(self, root) -> None:
        self.root = root
        self.root.config(background="white")
        self.root.title("Fanatic")

        self.team_manager = TeamManager()

        self.form_frame = tk.Frame(self.root, background="white")
        self.stats_frame = tk.Frame(self.root, background="white")

        create_header(self.root, "Fanatic")
        self.age_field = FieldFactory(self.form_frame, "Ingrese su edad:")
        self.radio_grp = RadioGroup(
            self.form_frame, "Selecciona un equipo:", self.teams
        )
        self.selected_gender = RadioGroup(
            self.form_frame, "Seleccione su género:", ["Femenino", "Masculino"]
        )
        self.form_frame.pack(padx=10, pady=10)

        self.create_stats_frame()
        self.stats_frame.pack(padx=10, pady=10)

        create_submit_button(self.form_frame, self.submit_handler)

    def create_stats_frame(self):
        self.stats_label = tk.Label(
            self.stats_frame,
            text="Estadísticas de los Equipos",
            font=("Arial", spacing.base, "bold"),
            background="white",
            justify="left",
        )
        self.stats_label.pack(anchor="w", pady=spacing.gap_1)

        self.fans_leo = create_label(
            self.stats_frame,
            "Fanaticos del equipo Leones 0 , con una edad prodemio de N/A",
            spacing.sm,
        )

        self.fans_nav = create_label(
            self.stats_frame,
            "Fanaticos del equipo Navegantes 0 , con una edad prodemio de N/A",
            spacing.sm,
        )

        self.fans_tig = create_label(
            self.stats_frame,
            "Fanaticos del equipo Tigres 0, con una edad prodemio de N/A",
            spacing.sm,
        )

        self.avr_age_male = create_label(
            self.stats_frame, "Edad promedio de los hombres: N/A", spacing.sm
        )

        self.avr_age_female = create_label(
            self.stats_frame, "Edad promedio de las mujeres: N/A", spacing.sm
        )

    def submit_handler(self):
        age = int(self.age_field.input_entry.get())
        team = self.radio_grp.radio_var.get()
        gender = self.selected_gender.radio_var.get()

        self.team_manager.addPerson(Person(age, gender), team)

        self.age_field.input_entry.delete(0, tk.END)
        self.update_stats()

    def update_stats(self):
        avr_female_age, avr_male_age = calc_avr_age_per_gender(
            self.team_manager.get_all_persons()
        )

        self.fans_leo.config(
            text=f"Fanaticos del equipo Leones {len(self.team_manager.leones)} , con una edad prodemio de {calc_avr_age(self.team_manager.leones)}"
        )

        self.fans_nav.config(
            text=f"Fanaticos del equipo Navegantes {len(self.team_manager.navegantes)} , con una edad prodemio de {calc_avr_age(self.team_manager.navegantes)}"
        )

        self.fans_tig.config(
            text=f"Fanaticos del equipo Tigres {len(self.team_manager.tigres)} , con una edad prodemio de {calc_avr_age(self.team_manager.tigres)}"
        )

        self.avr_age_male.config(text=f"Edad promedio de los hombres: {avr_male_age}")
        self.avr_age_female.config(
            text=f"Edad promedio de las mujeres: {avr_female_age}"
        )


root = tk.Tk()
app = FanaticApp(root)
root.mainloop()

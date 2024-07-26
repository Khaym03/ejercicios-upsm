import tkinter as tk


class PartyApp:

    # font sizes
    sm = 12
    md = 14
    base = 16
    lg = 18

    gap_1 = 8
    gap_2 = 16

    numOfPersons = []

    def __init__(self, root):
        self.root = root
        self.root.config(background="white")
        self.root.title("Party")

        self.form_frame = tk.Frame(self.root, background="white")
        self.stats_frame = tk.Frame(self.root, background="white")

        self.create_header()
        self.age_entry = self.field_factory("Ingrese su edad:")
        self.gender_var = self.radio_button_factory(
            "Seleccione su género:", ["Femenino", "Masculino"]
        )
        self.create_submit_button()
        self.form_frame.pack(padx=10, pady=10)

        self.create_stats_frame()
        self.stats_frame.pack(padx=10, pady=10)

    def create_header(self):
        header = tk.Label(
            self.root,
            text="Bienvenido a la fiesta",
            font=("Arial", self.lg),
            background="white",
            justify="left",
        )
        header.pack()

    def create_stats_frame(self):
        # Crear etiquetas para mostrar las estadísticas
        self.stats_label = tk.Label(
            self.stats_frame,
            text="Estadísticas de la Fiesta",
            font=("Arial", self.base, "bold"),
            background="white",
            justify="left",
        )
        self.stats_label.pack(anchor="w", pady=self.gap_1)

        self.total_label = tk.Label(
            self.stats_frame,
            text="Total de personas: 0",
            font=("Arial", self.sm),
            background="white",
            justify="left",
        )
        self.total_label.pack(anchor="w", pady=self.gap_1)

        self.female_label = tk.Label(
            self.stats_frame,
            text="Mujeres: 0",
            font=("Arial", self.sm),
            background="white",
            justify="left",
        )
        self.female_label.pack(anchor="w", pady=self.gap_1)

        self.male_label = tk.Label(
            self.stats_frame,
            text="Hombres: 0",
            font=("Arial", self.sm),
            background="white",
            justify="left",
        )
        self.male_label.pack(anchor="w", pady=self.gap_1)

        self.oldest_label = tk.Label(
            self.stats_frame,
            text="Persona más vieja: N/A",
            font=("Arial", self.sm),
            background="white",
            justify="left",
        )
        self.oldest_label.pack(anchor="w", pady=self.gap_1)

    def field_factory(self, name: str):
        field = tk.Frame(self.form_frame, background="white")

        # Crear la etiqueta y alinearla a la izquierda
        label = tk.Label(
            field,
            text=name,
            font=("Arial", self.base),
            justify="left",
            background="white",
        )
        label.pack(
            anchor="w",
            pady=self.gap_1,
        )

        # Crear la entrada y alinearla a la izquierda
        input_entry = tk.Entry(
            field,
            width=42,
            font=("Arial", self.md),
            background="white",
        )
        input_entry.pack(side=tk.LEFT, anchor="w")

        field.pack(anchor="w")  # Empaquetar el campo completo a la izquierda

        return input_entry

    def radio_button_factory(self, name: str, options: list):
        field = tk.Frame(self.form_frame, background="white")

        # Crear la etiqueta y alinearla a la izquierda
        label = tk.Label(
            field,
            text=name,
            font=("Arial", self.base),
            justify="left",
            background="white",
        )
        label.pack(anchor="w", pady=self.gap_1)

        # Crear el grupo de radio buttons
        self.radio_var = tk.StringVar(value=options[0])
        for option in options:
            radio_button = tk.Radiobutton(
                field,
                text=option,
                variable=self.radio_var,
                value=option,
                font=("Arial", self.base),
                background="white",
            )
            radio_button.pack(padx=5)

        field.pack(anchor="w")  # Empaquetar el campo completo a la izquierda

        return self.radio_var

    def create_submit_button(self):
        submit_button = tk.Button(
            self.form_frame,
            text="Enviar",
            font=("Arial", self.sm, "bold"),
            width=46,
            command=self.submit,
        )
        submit_button.pack(
            anchor="w",
            pady=self.gap_1,
        )

    def submit(self):
        age = int(self.age_entry.get())
        gender = self.gender_var.get()

        self.numOfPersons.append((age, gender))
        self.age_entry.delete(0, tk.END)

        self.update_stats()

    def update_stats(self):
        total = len(self.numOfPersons)
        female_count = sum(1 for _, gender in self.numOfPersons if gender == "Femenino")
        male_count = sum(1 for _, gender in self.numOfPersons if gender == "Masculino")
        oldest_age = max((age for age, _ in self.numOfPersons), default="N/A")

        # Actualizar las etiquetas
        self.total_label.config(text=f"Total de personas: {total}")
        self.female_label.config(text=f"Mujeres: {female_count}")
        self.male_label.config(text=f"Hombres: {male_count}")
        self.oldest_label.config(text=f"Persona más vieja: {oldest_age} años")


if __name__ == "__main__":
    root = tk.Tk()
    app = PartyApp(root)
    root.mainloop()

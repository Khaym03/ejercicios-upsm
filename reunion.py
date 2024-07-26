import tkinter as tk


class PartyApp:
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

        self.create_header()
        self.age_entry = self.field_factory("Ingrese su edad:")
        self.gender_var = self.radio_button_factory(
            "Seleccione su género:", ["Femenino", "Masculino"]
        )
        self.create_submit_button()
        self.form_frame.pack(padx=10, pady=10)

    def create_header(self):
        header = tk.Label(
            self.root,
            text="Bienvenido a la fiesta",
            font=("Arial", self.lg),
            background="white",
            justify="left",
        )
        header.pack()

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
            width=30,
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


if __name__ == "__main__":
    root = tk.Tk()
    app = PartyApp(root)
    root.mainloop()

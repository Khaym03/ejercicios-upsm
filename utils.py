import tkinter as tk


class Spacing:
    def __init__(self) -> None:
        self.sm = 12
        self.md = 14
        self.base = 16
        self.lg = 18
        self.gap_1 = 8
        self.gap_2 = 16


class Person():
    def __init__(self, age, gender) -> None:
        self.age = age
        self.gender = gender

spacing = Spacing()


def create_header(root: tk.Tk, header: str):
    header = tk.Label(
        root,
        text=header,
        font=("Arial", spacing.lg),
        background="white",
        justify="left",
    )
    header.pack()


def create_label(parent_frame: tk.Frame, name: str, font_size=spacing.base):
    label = tk.Label(
        parent_frame,
        text=name,
        font=("Arial", font_size),
        justify="left",
        background="white",
    )
    label.pack(anchor="w", pady=spacing.gap_1)
    return label


def create_submit_button(parent_frame: tk.Frame, handler):
    submit_button = tk.Button(
        parent_frame,
        text="Enviar",
        font=("Arial", spacing.sm, "bold"),
        width=46,
        command=handler,
    )
    submit_button.pack(
        anchor="w",
        pady=spacing.gap_1,
    )


class FieldFactory:
    def __init__(self, parent_frame: tk.Frame, name: str) -> None:
        self.field = tk.Frame(parent_frame, background="white")
        create_label(parent_frame, name)

        self.input_entry = tk.Entry(
            self.field,
            width=42,
            font=("Arial", spacing.md),
            background="white",
        )
        self.input_entry.pack(side=tk.LEFT, anchor="w")

        self.field.pack(anchor="w")


class RadioGroup:
    def __init__(self, parent_frame: tk.Frame, name: str, options: list) -> None:
        field = tk.Frame(parent_frame, background="white")

        create_label(parent_frame, name)

        # Crea un grupo de radio buttons
        self.radio_var = tk.StringVar(value=options[0])
        for option in options:
            radio_button = tk.Radiobutton(
                field,
                text=option,
                variable=self.radio_var,
                value=option,
                font=("Arial", spacing.base),
                background="white",
            )
            radio_button.pack(padx=5, anchor="w")

        field.pack(anchor="w")


def calc_avr_age_per_gender(persons: list[Person]):
    female_count = male_count = 0
    female_total_age = male_total_age = avr_female_age = avr_male_age = 0

    for person in persons:
      
        if person.gender == "Femenino":
            female_count += 1
            female_total_age += person.age

        if person.gender == "Masculino":
            male_count += 1
            male_total_age += person.age

    if female_count != 0:
        avr_female_age = female_total_age / female_count

    if male_count != 0:
        avr_male_age = male_total_age / male_count

    return (avr_female_age, avr_male_age)



def calc_avr_age(persons: list[Person]):
    totalAge = sum(person.age for person in persons)
    
    if len(persons) > 0:
        return totalAge / len(persons)
    
    return 0

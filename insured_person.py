class InsuredPerson:
    def __init__(self, first_name, last_name, age, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"{self.first_name} {self.last_name}, věk: {self.age}, telefon: {self.phone}"
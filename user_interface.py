from insured_person import InsuredPerson

class UserInterface:
    def __init__(self, database):
        self.db = database

    def run(self):
        while True:
            self.show_menu()
            choice = input("Zvolte akci: ")
            print()
            if choice == "1":
                self.add_person()
            elif choice == "2":
                self.list_people()
            elif choice == "3":
                self.find_person()
            elif choice == "4":
                print("Ukončuji aplikaci.")
                break
            else:
                print("Neplatná volba.\n")

    def show_menu(self):
        print("Pojištění – Evidence")
        print("1. Přidat pojištěného")
        print("2. Zobrazit všechny pojištěné")
        print("3. Vyhledat pojištěného")
        print("4. Konec\n")

    def add_person(self):
        first_name = self.get_input("Zadejte jméno: ", required=True)
        last_name = self.get_input("Zadejte příjmení: ", required=True)
        age = self.get_input("Zadejte věk: ", numeric=True)
        phone = self.get_input("Zadejte telefon: ", required=True)
        person = InsuredPerson(first_name, last_name, age, phone)
        self.db.add_person(person)
        print("Pojištěný byl přidán.\n")

    def list_people(self):
        people = self.db.list_people()
        if not people:
            print("Seznam je prázdný.\n")
        else:
            for person in people:
                print(person)
            print()

    def find_person(self):
        first_name = self.get_input("Zadejte jméno: ", required=True)
        last_name = self.get_input("Zadejte příjmení: ", required=True)
        results = self.db.find_person(first_name, last_name)
        if results:
            for person in results:
                print(person)
        else:
            print("Pojištěný nenalezen.")
        print()

    def get_input(self, prompt, required=False, numeric=False):
        while True:
            value = input(prompt)
            if required and not value.strip():
                print("Tato hodnota je povinná.")
                continue
            if numeric:
                if not value.isdigit():
                    print("Zadejte prosím číslo.")
                    continue
                return int(value)
            return value
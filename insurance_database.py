class InsuranceDatabase:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def list_people(self):
        return self.people

    def find_person(self, first_name, last_name):
        return [
            person for person in self.people
            if person.first_name.lower() == first_name.lower()
            and person.last_name.lower() == last_name.lower()
        ]
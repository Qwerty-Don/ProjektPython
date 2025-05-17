from insurance_database import InsuranceDatabase
from user_interface import UserInterface

def main():
    db = InsuranceDatabase()
    ui = UserInterface(db)
    ui.run()

if __name__ == "__main__":
    main()
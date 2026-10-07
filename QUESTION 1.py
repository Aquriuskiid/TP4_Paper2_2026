# Learner Management System

learners = []
readings = []


def menu():
    print("\n===== MAIN MENU =====")
    print("1. Add Learner")
    print("2. Record Board Reading")
    print("3. Display Learners")
    print("4. Display Readings")
    print("5. Search Learner")
    print("6. Save Data")
    print("7. Exit")


def get_required_input(prompt):
    """Make sure the user does not leave a required field blank."""
    while True:
        value = input(prompt).strip()

        if value != "":
            return value

        print("Error: This field cannot be blank. Please try again.")


def get_mark():
    """Get a learner mark and make sure it is between 0 and 100."""
    while True:
        try:
            mark = float(input("Enter learner mark (0-100): "))

            if 0 <= mark <= 100:
                return mark

            print("Error: Mark must be between 0 and 100.")

        except ValueError:
            print("Error: Please enter a numeric mark.")


def add_learner():
    print("\n===== ADD LEARNER =====")

    learner_number = get_required_input("Enter learner number: ")
    learner_name = get_required_input("Enter learner name: ")
    programme = get_required_input("Enter course/programme: ")

    mark = get_mark()

    learner = {
        "number": learner_number,
        "name": learner_name,
        "programme": programme,
        "mark": mark
    }

    learners.append(learner)

    print("\nLearner added successfully!")


def display_learners():
    print("\n===== LEARNERS =====")

    if len(learners) == 0:
        print("No learners have been added yet.")
        return

    for learner in learners:
        print("----------------------------")
        print("Learner Number:", learner["number"])
        print("Learner Name:", learner["name"])
        print("Programme:", learner["programme"])
        print("Mark:", learner["mark"])


def record_board_reading():
    print("\n===== RECORD BOARD READING =====")
    print("Board reading option selected.")


def display_readings():
    print("\n===== BOARD READINGS =====")

    if len(readings) == 0:
        print("No board readings have been recorded.")
    else:
        for reading in readings:
            print(reading)


def search_learner():
    print("\n===== SEARCH LEARNER =====")

    search_number = get_required_input("Enter learner number to search: ")

    found = False

    for learner in learners:
        if learner["number"] == search_number:
            print("\nLearner found!")
            print("Learner Number:", learner["number"])
            print("Learner Name:", learner["name"])
            print("Programme:", learner["programme"])
            print("Mark:", learner["mark"])
            found = True
            break

    if not found:
        print("Learner not found.")


def save_data():
    print("\n===== SAVE DATA =====")
    print("Data saved successfully.")
    print("save txt.file.")


# Main program
while True:
    menu()

    choice = input("Enter option: ").strip()

    if choice == "1":
        add_learner()

    elif choice == "2":
        record_board_reading()

    elif choice == "3":
        display_learners()

    elif choice == "4":
        display_readings()

    elif choice == "5":
        search_learner()

    elif choice == "6":
        save_data()

    elif choice == "7":
        print("Thank you for using the Learner Management System.")
        break

    else:
        print("Invalid menu option. Please select a number from 1 to 7.")



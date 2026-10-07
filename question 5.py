import csv
from datetime import datetime

learners = []
readings = []


# Save learners to CSV
def save_learners():
    file = open("learners.csv", "w", newline="")
    writer = csv.writer(file)

    writer.writerow(["Learner Number", "Name", "Programme", "Mark"])

    for learner in learners:
        writer.writerow(learner)

    file.close()


# Load learners from CSV
def load_learners():
    try:
        file = open("learners.csv", "r")
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            try:
                row[3] = float(row[3])
                learners.append(row)
            except ValueError:
                print("There is an invalid mark in the file.")

        file.close()

    except FileNotFoundError:
        print("No learner file found.")


# Save readings to CSV
def save_readings():
    file = open("reading.csv", "w", newline="")
    writer = csv.writer(file)

    writer.writerow(["Date and Time", "Reading"])

    for reading in readings:
        writer.writerow(reading)

    file.close()


# Load readings from CSV
def load_readings():
    try:
        file = open("reading.csv", "r")
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            try:
                row[1] = float(row[1])
                readings.append(row)
            except ValueError:
                print("There is an invalid reading in the file.")

        file.close()

    except FileNotFoundError:
        print("No reading file found.")


# Add a learner
def add_learner():
    number = input("Enter learner number: ")
    name = input("Enter learner name: ")
    programme = input("Enter programme: ")

    try:
        mark = float(input("Enter mark: "))

        if mark >= 0 and mark <= 100:
            learners.append([number, name, programme, mark])
            save_learners()
            print("Learner saved.")
        else:
            print("Mark must be between 0 and 100.")

    except ValueError:
        print("Please enter a number for the mark.")


# Add a sensor reading
def add_reading():
    try:
        reading = float(input("Enter sensor reading: "))

        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        readings.append([date_time, reading])
        save_readings()

        print("Reading saved.")

    except ValueError:
        print("Please enter a number.")


# Show number of records
def show_records():
    print("Number of learners:", len(learners))
    print("Number of readings:", len(readings))


# Load old data when program starts
load_learners()
load_readings()


# Main menu
while True:
    print("\n===== MENU =====")
    print("1. Add Learner")
    print("2. Add Sensor Reading")
    print("3. Show Number of Records")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_learner()

    elif choice == "2":
        add_reading()

    elif choice == "3":
        show_records()

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")


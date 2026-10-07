
# List to store multiple learner records
learners = [
    {
        "number": "1001",
        "name": "John",
        "programme": "IT",
        "marks": [70, 80, 90]
    },
    {
        "number": "1002",
        "name": "Mary",
        "programme": "Business",
        "marks": [65, 55, 70]
    },
    {
        "number": "1003",
        "name": "Peter",
        "programme": "Engineering",
        "marks": [40, 45, 35]
    }
]


# Function to calculate the average mark
def calculate_average(marks):
    return sum(marks) / len(marks)


# Function to assign Pass or Fail status
def get_status(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


# Function to search for a learner by learner number
def search_learner(learner_number):
    for learner in learners:
        if learner["number"] == learner_number:
            print("\nLearner Found")
            print("------------------------")
            print("Learner Number:", learner["number"])
            print("Name:", learner["name"])
            print("Programme:", learner["programme"])
            print("Marks:", learner["marks"])

            average = calculate_average(learner["marks"])
            status = get_status(average)

            print("Average:", round(average, 2))
            print("Status:", status)
            return

    print("Learner not found.")


# Function to display all learners
def display_all_learners():
    print("\nALL LEARNERS")
    print("-" * 75)

    print(f"{'Number':<10}{'Name':<15}{'Programme':<15}{'Average':<12}{'Status':<10}")
    print("-" * 75)

    for learner in learners:
        average = calculate_average(learner["marks"])
        status = get_status(average)

        print(
            f"{learner['number']:<10}"
            f"{learner['name']:<15}"
            f"{learner['programme']:<15}"
            f"{average:<12.2f}"
            f"{status:<10}"
        )

    print("-" * 75)


# Display all learners
display_all_learners()

# Search for a learner
search_number = input("\nEnter learner number to search: ")
search_learner(search_number)


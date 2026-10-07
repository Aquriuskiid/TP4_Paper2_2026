class Learner:
    def __init__(self, number, name, programme, marks):
        self.number = number
        self.name = name
        self.programme = programme
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def status(self):
        if self.average() >= 50:
            return "Pass"
        else:
            return "Fail"

    def display(self):
        print("Learner Number:", self.number)
        print("Name:", self.name)
        print("Programme:", self.programme)
        print("Marks:", self.marks)
        print("Average:", self.average())
        print("Status:", self.status())


learner1 = Learner("1001", "John", "IT", [70, 80, 90])
learner2 = Learner("1002", "Mary", "Business", [55, 60, 65])
learner3 = Learner("1003", "Peter", "Computer Science", [40, 45, 35])

learners = [learner1, learner2, learner3]


while True:
    print("\n1. Display Learners")
    print("2. Search Learner")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for learner in learners:
            learner.display()
            print()

    elif choice == "2":
        number = input("Enter learner number: ")

        for learner in learners:
            if learner.number == number:
                learner.display()
                break
        else:
            print("Learner not found")

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid choice")

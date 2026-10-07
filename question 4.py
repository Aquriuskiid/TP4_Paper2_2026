from random import randint
from datetime import datetime
import csv
import os

def temperature():
    return randint(10, 40)

def light():
    return randint(0, 100)

def check_temp(temp):
    if temp >= 18 and temp <= 30:
        return "NORMAL"
    else:
        return "ALERT"

def save_reading(learner, temp, light_level):
    time = datetime.now()
    status = check_temp(temp)

    with open("readings.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([learner, time, temp, light_level, status])

learner = input("Enter learner number: ")

temp = temperature()
light_level = light()

print("Temperature:", temp, "C")
print("Light level:", light_level)
print("Temperature status:", check_temp(temp))

save_reading(learner, temp, light_level)

print("Reading saved.")

if os.path.exists("readings.csv"):
    print("\nPrevious readings:")
    with open("readings.csv", "r") as file:
        for line in file:
            print(line.strip())

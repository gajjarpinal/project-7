import datetime
import time
import math
import random
import uuid

def date_time():

    print("\nDate and Time")
    print("1. Current Date")
    print("2. Current Time")
    print("3. Countdown")
    print("4. Back")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("Date :", datetime.date.today())

    elif choice == 2:
        print("Time :", datetime.datetime.now().strftime("%H:%M:%S"))

    elif choice == 3:
        sec = int(input("Enter Seconds: "))

        while sec > 0:
            print(sec)
            time.sleep(1)
            sec -= 1

        print("Time Over")

def maths():
    print("\nMath Menu")
    print("1. Square Root")
    print("2. Power")
    print("3. Circle Area")
    print("4. Factorial")
    print("5. Back")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        n = int(input("Enter Number: "))
        print("Answer =", math.sqrt(n))

    elif choice == 2:
        a = int(input("Enter Number: "))
        b = int(input("Enter Power: "))
        print("Answer =", math.pow(a, b))

    elif choice == 3:
        r = float(input("Enter Radius: "))
        print("Area =", round(math.pi * r * r, 2))

    elif choice == 4:
        n = int(input("Enter Number: "))
        print("Factorial =", math.factorial(n))

def random_data():
    print("\nRandom Menu")
    print("1. Random Number")
    print("2. Dice")
    print("3. OTP")
    print("4. Back")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print(random.randint(1, 50))

    elif choice == 2:
        print("Dice =", random.randint(1, 6))

    elif choice == 3:
        print("OTP =", random.randint(100000, 999999))


def uuid_code():
    print("UUID :", uuid.uuid4())

def file_menu():
    print("\nFile Menu")
    print("1. Create File")
    print("2. Write File")
    print("3. Read File")
    print("4. Back")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        name = input("File Name: ")
        file = open(name, "w")
        file.close()
        print("File Created")

    elif choice == 2:
        name = input("File Name: ")
        data = input("Enter Data: ")

        file = open(name, "w")
        file.write(data)
        file.close()

        print("Data Saved")

    elif choice == 3:
        name = input("File Name: ")

        file = open(name, "r")
        print(file.read())
        file.close()

while True:
    print("\nMulti Utility Toolkit")
    print("1. Date and Time")
    print("2. Math")
    print("3. Random")
    print("4. UUID")
    print("5. File")
    print("6. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        date_time()

    elif ch == 2:
        maths()

    elif ch == 3:
        random_data()

    elif ch == 4:
        uuid_code()

    elif ch == 5:
        file_menu()

    elif ch == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
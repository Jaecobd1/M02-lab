# Author: Jake Dobler
# M02-lab.py
# This app will tell if a student is on the honor roll and or
# on the deans list given the student's name and gpa.
while True:
    last_name = input("Student's last name:")
    if last_name == "zzz":
        break
    else:
        first_name = input("Student's first name:")
        gpa = float(input("Student's GPA:"))
        if (gpa >= 3.25):
            print(first_name + " " + last_name + " has made the Honor Roll.")
            if (gpa >= 3.5):
                print(first_name + " " + last_name +
                      " has made the Dean's List.")
                break
            else:
                break
        else:
            print(first_name + " " + last_name +
                  " did not qualify for anything this semester.")
            break

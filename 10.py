print("STUDENT GRADE EVALUATION SYSTEM")

name = input("Enter student name: ")
marks = int(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks!")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Grade: Fail")

if 0 <= marks <= 100:
    print("Student Name:", name)
    print("Marks:", marks)

students = {
    "anusha": {"roll_number": 45, "marks": 85},
    "renuka": {"roll_number": 64, "marks": 92},
    "anitha": {"roll_number": 25, "marks": 78},
    "sindhu": {"roll_number": 67,  "marks": 90},
    "sinchu":  {"roll_number": 56,  "marks": 30}
    }

def calculate_result(marks):
    if marks >= 60:
        return "Pass"
    else:
        return "Fail"

def display_student_info(student_name):
    if student_name in students:
        student_info = students[student_name]
        roll_number = student_info["roll_number"]
        marks = student_info["marks"]
        result = calculate_result(marks)
        print(f"Name: {student_name}")
        print(f"Roll Number: {roll_number}")
        print(f"Marks: {marks}")
        print(f"Result: {result}")
    else:
        print("Student not found.")
student_name = input("Enter the name of the student: ")
display_student_info(student_name)


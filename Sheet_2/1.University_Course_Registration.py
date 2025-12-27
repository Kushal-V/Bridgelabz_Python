# a student has a list of grades

class Course:
    def __init__(self,name,max_capacity):
        self.name = name
        self.max_capacity = max_capacity    
        self.students = []
    
class Student:
    def __init__(self,name,list_of_grades):
        self.name = name
        self.list_of_grades = list_of_grades

    def calculate_gpa(self):
        return sum(self.list_of_grades) / len(self.list_of_grades)

class Registration:
    def enroll(self,student,course):
        if student.calculate_gpa() > 3.0 and len(course.students) < course.max_capacity:
            course.students.append(student)
            return True
        return False

students = [
    Student("Kushal", [4.0, 3.5, 4.0]),
    Student("Aditya", [2.0, 3.0, 2.5]),
    Student("Gaurish", [3.0, 3.5, 4.0])
]

advance_ai = Course("Advance AI", 2)

registration = Registration()

eligible_stu = [
    student for student in students if student.calculate_gpa() > 3.0
]
for student in eligible_stu:
    registration.enroll(student,advance_ai)

print(f"Students enrolled in {advance_ai.name}: {advance_ai.students}")
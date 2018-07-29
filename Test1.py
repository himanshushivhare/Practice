class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return repr((self.name, self.age, self.grade))


student_objects = [
        Student('John', 'A', 15),
        Student('jane', 'B', 12),
        Student('Dave', 'B', 10),
        Student('himanshu', 'D', 20),
        Student('Himanshu', 'D', 20)
]
print student_objects
sorted_students = sorted(student_objects, key=lambda student: student.name.lower(), reverse=True)

print sorted_students
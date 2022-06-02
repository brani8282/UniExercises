class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class Group:
    def __init__(self, list_students):
        self.list_students = list_students

    def add_student(self, student):
        self.list_students.append(student)

    def remove_student(self):
        for i in range(0, len(self.list_students) - 1):
            if self.list_students[i].grade == 2:
                self.list_students.pop(i)

    # def avg(self):
    #     for i in range(0, len(list_students) - 1):


student1 = Student("Ivan Ivanov", 2)
student2 = Student("Yordan Ivan", 6)
student3 = Student("Mitko Ivanov", 4)
student4 = Student("Kur Zatrapov", 2)

listOfStudents = [student1, student2, student3]
group45 = Group(listOfStudents)
group45.remove_student()
group45.add_student(student4)
print(group45.list_students[2].name)
from abc import ABC, abstractmethod


# Parent class - Abstraction
class Student(ABC):

    def __init__(self, name, roll_no):
        # Private attributes - Encapsulation
        self.__name = name
        self.__roll_no = roll_no

    # Getter methods
    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    # Abstract method
    @abstractmethod
    def display_info(self):
        pass


# Child class - Inheritance
class SchoolStudent(Student):

    def display_info(self):
        print("School Student")
        print("Name:", self.get_name())
        print("Roll No:", self.get_roll_no())
        print()


# Child class - Inheritance
class CollegeStudent(Student):

    def display_info(self):
        print("College Student")
        print("Name:", self.get_name())
        print("Roll No:", self.get_roll_no())
        print()


# Creating objects
student1 = SchoolStudent("Rahul", 101)
student2 = SchoolStudent("Priya", 102)

student3 = CollegeStudent("Aman", 201)
student4 = CollegeStudent("Neha", 202)


# Store all objects in one list
students = [student1, student2, student3, student4]


# Polymorphism
for student in students:
    student.display_info()

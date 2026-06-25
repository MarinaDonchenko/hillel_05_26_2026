class Student:
    class_name = "Student"
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Average_score: {self.average_score}")
    def change_average_score(self, new_average_score):
        self.average_score = new_average_score
student = Student("Marina", "Donchenko", 35, 4.8)
print("Info about student:")
student.display_info()

student.change_average_score(5)

print("\nInfo about student after changed average score:")
student.display_info()
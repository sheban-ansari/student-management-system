class Student:

    all_students = []

    def __init__(self, name, roll_number, marks):
        self.name = name 
        self.roll_number = roll_number
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks

    def show_details(self):
        print("\n Student Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

    @classmethod
    def find_student_by_roll(cls, roll):
        for student in cls.all_students:
            if student.roll_number == roll:
                return student
        return None
    
    @classmethod
    def show_all_students(cls):
        if not cls.all_students:
            print("No Student Found")
            return
        for student in cls.all_students:
            student.show_details()


    @classmethod
    def add_students(cls):
        name = input("Enter Student's Name: ")
        roll = input("Enter Student's Roll Number: ")
        marks = int(input("Enter Student's Marks: "))
        student = cls(name, roll, marks)
        cls.all_students.append(student)
        print(f"Student {name} Added Successfully!")

    @classmethod
    def update_student_marks(cls):
        roll = input("Enter Student's Roll Number To Update Marks: ")
        student = cls.find_student_by_roll(roll)
        if student:
            new_marks = int(input("Enter New Marks: "))
            student.update_marks(new_marks)
            print(f"Marks for {student.name} Updated Successfully!")
        else:
            print("Student Not Found")

def menu():
        while True:
            print("\n =============== Student Management System ===============")
            print("1. Add Student")
            print("2. Update Marks")
            print("3. Show All Student")
            print("4. Exit")

            choice = int(input("Enter Your Option (1-4): "))
            if choice == 1:
                Student.add_students()
            elif choice == 2:
                Student.update_student_marks()
            elif choice == 3:
                Student.show_all_students()
            elif choice == 4:
                print("Exiting Student Managent System, Goodbye!")
                break
            else:
                print("Invalid Choice. Please Try Again!")

if __name__ == "__main__":
    menu()
class Student:
    def __init__(self):
        self.roll_no = input("\n\tEnter the Student Roll Number: ")
        self.name = input("\tEnter the Student Name: ")
        self.phone_number = input("\tEnter the Student Phone Number: ")
        student_class = input("\tEnter the Student Class [Ex: 1 2 3 4 5 6 7 8 9 10]: ")

        if student_class in StudentClass.classes:
            StudentClass.classes[student_class].studentList.append(self)
        else:
            new_class = StudentClass(student_class)
            new_class.studentList.append(self)
            StudentClass.classes[student_class] = new_class

        self.student_class = StudentClass.classes[student_class]

    def display(self):
        print(f"\tRoll No: {self.roll_no}, Name: {self.name}, Phone: {self.phone_number}, Class: {self.student_class.name}")


class StudentClass:
    classes = {}

    def __init__(self, name):
        self.name = name
        StudentClass.classes[name] = self
        self.studentList = []


class School:
    school_name = "ABC School"

    @staticmethod
    def get_all_students():
        for class_name, student_class in StudentClass.classes.items():
            print(f"\nClass: {class_name}")
            if not student_class.studentList:
                print("\tNo Students in this Class.")
            else:
                for student in student_class.studentList:
                    student.display()

    @staticmethod
    def get_student_by_roll(roll_no):
        for student_class in StudentClass.classes.values():
            for student in student_class.studentList:
                if student.roll_no == roll_no:
                    return student
        return None


def main():
    while True:
        print(f"\n--- Welcome To {School.school_name} ---\n")
        print("\t1) To Get Student Details")
        print("\t2) To Add New Student")
        print("\t3) To Remove Student")
        print("\t4) To Update Student Details")
        print("\t5) To Update School Name")
        print("\t6) To Get Number of Students in School")
        print("\t7) To Get All Students Details")
        print("\t8) To Get Any Student's Details")
        print("\t9) Exit")

        option = input("\nEnter Any Above Given Option: ")
        print()

        if option == "1":
            roll_no = input("\tEnter Roll Number of Student: ")
            student = School.get_student_by_roll(roll_no)
            if student:
                student.display()
            else:
                print("\tStudent not found!")

        elif option == "2":
            Student()
            print("\tStudent Added Successfully!")

        elif option == "3":
            roll_no = input("\tEnter Roll Number of Student to Remove: ")
            student = School.get_student_by_roll(roll_no)
            if student:
                student.student_class.studentList.remove(student)
                print("\tStudent Removed Successfully!")
            else:
                print("\tStudent not found!")

        elif option == "4":
            roll_no = input("\tEnter Roll Number of Student to Update: ")
            student = School.get_student_by_roll(roll_no)
            if student:
                print("\tLeave blank if you don’t want to update.")
                new_name = input("\tEnter New Name: ")
                new_phone = input("\tEnter New Phone Number: ")
                new_class = input("\tEnter New Class: ")

                if new_name:
                    student.name = new_name
                if new_phone:
                    student.phone_number = new_phone
                if new_class:
                    student.student_class.studentList.remove(student)
                    if new_class not in StudentClass.classes:
                        StudentClass.classes[new_class] = StudentClass(new_class)
                    StudentClass.classes[new_class].studentList.append(student)
                    student.student_class = StudentClass.classes[new_class]

                print("\tStudent Details Updated Successfully!")
            else:
                print("\tStudent not found!")

        elif option == "5":
            new_name = input("\tEnter New School Name: ")
            if new_name:
                School.school_name = new_name
                print("\tSchool Name Updated Successfully!")

        elif option == "6":
            total = sum(len(sc.studentList) for sc in StudentClass.classes.values())
            print(f"\tTotal Students in School: {total}")

        elif option == "7":
            School.get_all_students()

        elif option == "8":
            roll_no = input("\tEnter Roll Number: ")
            student = School.get_student_by_roll(roll_no)
            if student:
                student.display()
            else:
                print("\tStudent not found!")

        elif option == "9":
            print("\tExiting Program... Goodbye!")
            break

        else:
            print("\tInvalid Option! Please try again.")


if __name__ == "__main__":
    main()

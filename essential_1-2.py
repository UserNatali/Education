class Scool:
    count = 0
    def __init__(self, name, age, class_student, teacher, delight):
        self.name = name
        self.age = age
        self.class_student = class_student
        self.teacher = teacher
        self.delight = delight
        Scool.count += 1

    def __repr__(self):
        return f"{self.__dict__}"

    def __del__(self):
        print()

    def input_object(self):
        self.name = input("Input name")
        self.age = int(input("Input age"))
        self.class_student = input("Input class_student")
        self.teacher = input("Input teacher")
        self.delight = input("Input delight")
        return Scool(self.name, self.age, self.class_student, self.teacher, self.delight)



student1 = Scool("Ivan", 15, "9a", "Krilov A.", "tennis")
student2 = Scool("Maria", 9, "3a", "Veklyk A.", "checkers")
student3 = Scool("Alex", 11, "5b", "Mishina M.", "dance")
student4 = Scool("Leon", 12, "6c", "Koval Y.", "football")


#for i in range(Scool.count):
 #   list_student.append(__object=Scool.__dict__)

#print(list_student)
list_student = [student1, student2, student3, student4]
print(list_student)


def sort_my(list_student):
    return list_student["name"]


list_student_sort = sorted(list_student, key=sort_my)

def menu():
    while True:
        print("1. Add student\n2. Delete student\n3. Print list of student\n4.Sorting\n5.Exit\n")
        choice = input("Make your choice: ")
        if choice == "1":
            name = input("Input name")
            age = int(input("Input age"))
            class_student = input("Input class_student")
            teacher = input("Input teacher")
            delight = input("Input delight")
            student = Scool(name, age, class_student, teacher, delight)
            list_student.append(student)
            print(list_student)
        elif choice == "2":
            student_del = input("Which object will be deleted?")
            for i in list_student:
                if i.name == student_del:
                    print(i)
                    list_student.remove(i)
                    print(list_student)
        elif choice == "3":
            print(list_student)
        elif choice == "4":
            pass

        elif choice == "5":
            break


menu()


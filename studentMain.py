import studentController as sc
studentController = sc.StudentController()

while True:
    print("STUDENT CRUD")
    print("----------------------------")
    print("1.- Add a student")
    print("2.- Delete a student")
    print("3.- Modify a student")
    print("4.- Search a student")
    print("5.- Exit")
    option=int(input("Choose option:"))

    if option ==1:
        dni = input("Insert DNI:")
        if studentController.checkingDNI(dni):
            name = input("Insert name:")
            surnames = input("Insert surnames:")
            age = int(input("Insert age:"))
            city = input("Insert city:")
            province = input("Insert province:")
            email = input("Insert email:")
            if studentController.addStudent(dni, name, surnames, age, city, province, email):
                print("Student added!!")
            else:
                print("DNI exists!!")
        else:
            print("DNI is not correct!!")

    if option ==2:
        dni = input("Insert DNI: ")
        if studentController.delStudent(dni) is not None:
            print("Student deleted!!")
        else:
            print("DNI doesn't exists!!")

    if option ==3:
        dni = input("Insert DNI: ")
        student = studentController.searchStudent(dni)
        if student is not None:
            print("1.- Modify Name")
            print("2.- Modify Surnames")
            print("3.- Modify Age")
            print("4.- Modify City")
            print("5.- Modify Province")
            print("6.- Modify Email")
            modification=int(input("What do you want to modify:"))
            newValue = input("Insert the new value: ")
            studentController.modStudent(student,modification, newValue)
        else:
            print("DNI not found!!")
    if option ==4:
        dni = input("Insert DNI: ")
        student = studentController.searchStudent(dni)
        if student != None:
            print(student.getDNI())
            print(student.getName())
            print(student.getSurnames())
            print(student.getAge())
            print(student.getCity())
            print(student.getProvince())
            print(student.getEmail())
        else:
            print("DNI not found!!")
    if option ==5:
        print("Bye!!")
        break
print("Bye!!")
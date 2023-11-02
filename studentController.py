import student as st
class StudentController():
    def __init__(self):
        self.__students = {}
    
    def addStudent(self, dni, name, surnames, age, city, province, email):
        if dni not in self.__students:
            student = st.Student(dni, name, surnames, age, city, province, email)
            self.__students[dni]=student
            return True
        return False
    
    def delStudent(self, dni):
        if dni in self.__students:
            student = self.__students.pop(dni)
            return student
        return None
    
    def modStudent(self, student, modification, newValue):
        if modification == 1:
            student.setName(newValue)
            return student
        if modification == 2:
            student.setSurnames(newValue)
            return student
        if modification == 3:
            student.setAge(newValue)
            return student
        if modification == 4:
            student.setCity(newValue)
            return student
        if modification == 5:
            student.setProvince(newValue)
            return student
        if modification == 6:
            student.setEmail(newValue)
            return student

    def searchStudent(self, dni):
        if dni in self.__students:
            student = self.__students[dni]
            return student
        return None
    
    def checkingDNI(self,dni):
        letter = dni[-1]
        number=int(dni[0:8])
        word='TRWAGMYFPDXBNJZSQVHLCKE'
        Realletter = word[number%23]
        if(letter == Realletter):
            return True
        else:
            return False

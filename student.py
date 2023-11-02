class Student:
    def __init__(self, dni, name, surnames, age, city, province, email):
        self.__DNI = dni
        self.__Name = name
        self.__Surnames = surnames
        self.__Age = age
        self.__City = city
        self.__Province = province
        self.__Email = email

    def getDNI(self):
        return self.__DNI
    
    def setName(self, name):
        self.__Name = name
    def getName(self):
        return self.__Name
    
    def setSurnames(self, surnames):
        self.__Surnames = surnames
    def getSurnames(self):
        return self.__Surnames
    
    def setAge(self, age):
        self.__Age = age
    def getAge(self):
        return self.__Age
    
    def setCity(self, city):
        self.__City = city
    def getCity(self):
        return self.__City
    
    def setProvince(self, province):
        self.__Province = province
    def getProvince(self):
        return self.__Province
    
    def setEmail(self, email):
        self.__Email = email
    def getEmail(self):
        return self.__Email
    
class Student:
    def __init__(self, name, email):
        self.__details(name, email)
        
    def __details(self,name,email):
        self.name = name
        self.email = email
        
    def access(self):
        print(self.name)
        print(self.email)
        
    def __first(self):
        print("first")
        
    def second(self):
        self.__first()
        
std1 = Student("jyoti","jyoti12@gmail.com")
std1.access()
std1.second()
        
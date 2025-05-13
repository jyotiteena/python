class Student:
    name = "jyoti jingar"
    # def __init__(self,name):
    #     self.name = name  # can not change cls sttr value
        
    # first concept 
    # def changeName(self,name):
    #     Student.name = name # can change class attr value
    
    
    # second concept 
    def changeName(self,name):
        self.__class__.name = name
        
# s1 = Student("teena")
s1 = Student()
print(s1.name) # teena
print(Student.name) #jyoti jingar , can't change class attribute value

s1.changeName("mega")
print(s1.name)
print(Student.name)
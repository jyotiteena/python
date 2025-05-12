# create a constructor 

class Student:
    def __init__(self):
        print(self) #<__main__.Student object at 0x0000029A6AE06A50>
        print("added student details into database")

std = Student()

class Teacher :
           
    def __init__(self,username):
        self.username = username
        print(f"my name is {username}")
        
t1 = Teacher("jyoti")
print(t1.username) # jyoti

class Test :
           
    def __init__(abc,username):
        abc.username = username
        print(f"my name is {abc.username}")
        
test1 = Test("test jyoti") # attributes(test1)
print(test1.username) # jyoti

# without self parameter can't show output 


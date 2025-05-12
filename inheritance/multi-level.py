# types -> single,  multi-level and multiple 

class Teacher:
    @staticmethod
    def classRoom():
       print("class room")

    @staticmethod
    def labRoom():
        print("lab room")
        
class Student(Teacher):
    def __init__(self,grid):
       self.grid = grid
       
class Final(Student):
    def __init__(self,name):
       self.name = name
        
final1 = Final("jyoti")
print(final1.name)
final1.classRoom()
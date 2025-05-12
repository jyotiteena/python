# class Parent:
    
    
# class Child(Parent):

# base <- derived
# parent <- child

class Teacher:
    @staticmethod
    def classRoom():
       print("class room")

    @staticmethod
    def labRoom():
        print("lab room")
        
class Final(Teacher):
    def __init__(self,name):
       self.name = name
        
final1 = Final("jyoti")
print(final1.name)

final1.classRoom()
final1.labRoom()
        
    
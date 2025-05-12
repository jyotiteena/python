# class and instance attribute 

# class.attr 
# obj.attr 

class Teacher:
    teacher_college = "MBM" # class atrribute  use when value common and want to one memory location
    name = "jyoti jingar"
    def __init__(self,name):
        self.name = name  # object attribute
        
print(Teacher.teacher_college)  
t1 = Teacher("teena")
print(t1.name)
print(Teacher.name) # class attr
# print(Teacher.name) // error
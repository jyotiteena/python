# delete object and object properties

class Student:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no #public
        self.__acc_pass = acc_pass  # private
        print("delete concept")
        
    def reset_pass(self):
        print(self.__acc_pass)
        
s1 = Student(2323,"2323@12")
print(s1.acc_no)
s1.reset_pass() # 2323@12 can access 
print(s1.__acc_pass)

del s1
# print(s1) #name 's1' is not defined
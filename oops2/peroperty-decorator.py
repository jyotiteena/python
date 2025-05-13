class Student:
    def __init__(self,hindi,eng,maths):
        self.hindi =  hindi
        self.eng =  eng
        self.maths =  maths
        # self.per = str((self.hindi+self.eng+self.maths)/len([self.hindi,self.eng,self.maths])) + "%"
        
    @property
    def perMark(self):
        return str((self.hindi+self.eng+self.maths)/len([self.hindi,self.eng,self.maths])) + "%"
        
std1 = Student(90,80,70)
print(std1.perMark)
# print("per = ",std1.per)
std1.eng = 90
# print("per = ",std1.per) # can not change per according to std1.end = 90
print(std1.perMark)
class Student:
    def __init__(self,hindi,eng,maths):
        self.hindi =  hindi
        self.eng =  eng
        self.maths =  maths
        self.per = str((self.hindi+self.eng+self.maths)/len([self.hindi,self.eng,self.maths])) + "%"
        
std1 = Student(90,80,70)
print("per = ",std1.per)
std1.eng = 90
print(std1.eng)
print("per = ",std1.per) # can not change per according to std1.end = 90
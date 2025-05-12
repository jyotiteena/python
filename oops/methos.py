# class have two concept 
# data -  (attribute)
# methods - like function


class Student:
    def __init__(self,grid,marks):
        self.grid = grid
        self.marks = marks
        
    def show(self):
        print(f"my grid number is = {self.grid}")
        
    def avg(self):
        sum = 0
        for i in self.marks:
            sum+=i
        print(sum/len(self.marks))
        
std1 = Student(123,[99,98,97])
std1.show()
std1.avg()

std1.grid = 98989 # can be direct gird changed
std1.show() # my grid number is = 98989
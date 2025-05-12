# static method use because if you doesn't need self parameter 

# methods that don't use self parameter(work at class level)

class Stundet:
    @staticmethod # decorator
    def show():
        print("static method")
        
    @staticmethod # decorator
    def show2():
        print("static method2")
        
std1 = Stundet()
std1.show()
std1.show2()
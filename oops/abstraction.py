# abstraction - hiding the implementation details of a class and only showing is essential features of user 

# encapsulation - wrapping data and function into single unit(object)


class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.acc = True # hide
        self.clutch = True # hide
        print("start car")
        
car1 = Car()
car1.start()
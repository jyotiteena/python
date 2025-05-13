# __ (double score)  called dunder function 

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def show(self):
        print(f"{self.real}i + {self.img}j")
        
    def add(self,num2):
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real,new_img)    
    
c1 = Complex(12,2)
c1.show()
c2 = Complex(1,2)
c2.show()
result = c1.add(c2)
result.show()
    
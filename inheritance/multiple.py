class A:
    def __init__(self):
        print("class A")
        
class B(A):
    def __init__(self):
        super().__init__()
        print("class B and A")
        
class C(A):
    def __init__(self):
        super().__init__()
        print("class C and A")
        
b1 = B()
c1 = C()
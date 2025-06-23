a = 30 # this is global area

def display():
    a = 40
    print("local a = ",a) # local area 40
print("global a = ",a) #30
    
display()
print("global a = ",a) #30

# i want to global value when reflect into local variable 

b = 100
def show():
    global a, b
    b = 500
    print("local = ",b) # 500

print("global b = ",b) # 100
show()
print("global b = ",b) # 500

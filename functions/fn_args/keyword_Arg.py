def add(**values):
    print(values) #{'id': 123, 'name': 'jyoti'}
    
add(id=123,name="jyoti")

# / single and keyword arg mix /
def data(*arg1,**arg2):
    print(arg1)
    print(arg2)
    
data(1,2,3,id=123,name="jyoti")
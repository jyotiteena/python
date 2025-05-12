file = open('test.txt','w')

file.write("override data")

file = open('test.txt','a')
file.write("\nappend the data")

# / automatic create a file when i pass 'a' and 'w' 

open("jyoti.html",'w')
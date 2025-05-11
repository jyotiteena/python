# file I/O 
# type of files 
# text files (character format) :- .txt, .docx, .log etc.
# binary files (non-char format) :- mp4, .mov, .png, .jpeg

# syntax 
# open('file.txt/docx',mode)
# mode - r:read, w:write 

file = open("test.txt","r")

# output = file.read()
# print(output)
# print(type(output))


# output2 = file.read(10) #this is my
# print(output2)

output3 = file.readline()
print(output3) #this is my first program - only first line

output4 = file.readline()
print(output4) # second line exist - second line print


file.close()
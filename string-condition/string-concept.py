str1 = "hello"
str2  = 'world'

# its like pre tag
str3 = """
first
      second
"""
str4 = '''
    4th and 
    5th
'''
print(str1)
print(str2)
print(str3)
print(str4)

str5 = "it's a good person"
print(str5)

str6 = 'it"s a good person'
print(str6) #it"s a good person

str7 = "this is first para \n and second para is this"
print(str7)

str8 = "this is first para \t and second para is this"
print(str8)

# concat 
print(str1+ " " +str2)

print(len(str1))
print(str1[0])
print(str1[1])

# /// can't change character override or can't manupulate
# str1[0] = "s" error
# print(str1)


# most of methods use  in AI/ML
#  slicing 

# str[start_index:end_index ] --> end_index(ending index not included )

name = "jyoti jingar"
print(name[0:3]) # jyo
print(name[:3]) # jyo
print(name[1:])  #yoti jingar
print(name[1:len(name)])  #yoti jingar
print(name[6:13]) #jingar


# //// -ve index 
# jyoti -> j(-5), i(-1)
# -1 not included 
print(name[-3:-1]) #ga


a = 10
b = 20
print(f'sum of {a} & {b} = {a+b}')
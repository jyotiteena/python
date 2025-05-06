course = "web development web to web"
print(course.endswith("nt")) # True
print(course.endswith("nts")) # False
# print(course.capitalize())  # not reflect direct original string
course = course.capitalize() 
print(course)
print(course.replace("web","Website")) #Web development Website to Website
# find(), count()

print(course.find("dev")) # 4
print(course.count("web")) #2
print(course.count("Web")) # 1


# / check $ symobol how many time occurance from string 

dollar = "my price is $900 and other is $900"
print(dollar.count("$")) #2
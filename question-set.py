# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.

# ”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”

course = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(course)) # total 5 classrooms



# store 9, 9.0 seperate values into set 

values = {9,9.0,9.8}
print(values) # {9, 9.8} after decimal if 0(zero) then not count

# solution one is manually 
values2 = {9,"9.0"}
print(values2)


# solution second i build in methood
values3 = {
    ("float",9.0),
    ("int",9)
    }
print(values3) #{('float', 9.0), ('int', 9)}
# enter names of their 3 fav. movies & store them in list 
movie1 = input("enter first movie name = ")
movie2 = input("enter second movie name = ")
movie3 = input("enter third movie name = ")

# ///// method 1 - myself /////
movieList = [movie1,movie2,movie3]
print(movieList)

# ///// method 2 /////

movieList2 = []
movieList2.append(movie1)
movieList2.append(movie2)
movieList2.append(movie3)
print(movieList2)

# /////// method3 - same variable using /////

list1 = []
movie = input("enter first movie name = ")
list1.append(movie)
movie = input("enter second movie name = ")
list1.append(movie)
movie = input("enter third movie name = ")
list1.append(movie)

print("final movies")
print(list1)

# /////// method4 - same variable using /////
list2 = []
list2.append(input("enter first movie name = "))
list2.append(input("enter second movie name = "))
list2.append(input("enter third movie name = "))
print("list2 = ",list2)
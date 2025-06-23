print(abs(-100))

print(all([12,3,5])) # True

print(all([3,4,0])) #False because zero included

print(all([])) #True

# all => its like every in js 
#any => its like some in js
print(any((34,4,False))) # True
print(bin(15)) #0b1111

print(oct(15))

print(hex(15))

print(chr(97))
print(chr(65))
print(ord('A'))
print(ord('a'))
print(eval('23+3'))
eval("print('jyoti jingar')")
# help(str())

print(max([12,3,4,56]))
print(min([12,3,4,56]))
print(sum([1,2,3,4]))
print(pow(2,3))
# print(reversed([34,22,4]))
rev = reversed([23,4,5])
# print(rev)
for i in rev:
    print(i)
    
print(round(23.4))
print(round(23.58))

print(sorted([34,22,5,1,90,3]))
print(sorted([34,22,5,1,90,3],reverse=True))

key = ['id','name','grid']
values = [123,"jyoti",989]

print(zip(key,values)) #<zip object at 0x000001E0E81AF500>
print(dict(zip(key,values))) #{'id': 123, 'name': 'jyoti', 'grid': 989}
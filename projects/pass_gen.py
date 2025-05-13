import random
import string
print(random.choice(["A",'a',1]))
print(string.ascii_lowercase) #abcdefghijklmnopqrstuvwxyz
print(string.ascii_letters) # aabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 0123456789
print(string.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

randomValue = string.ascii_letters + string.digits + string.punctuation
print(randomValue)
print(random.choice(randomValue))

password = ""
for i in range(6):
    password+=random.choice(string.ascii_letters + string.digits)
    
print("your random password = ",password)
    
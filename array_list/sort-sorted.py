list1  = [34,5,6,7]

new_list = sorted(list1)
print(list1)
print(new_list)


new_list = sorted(list1,reverse=True)
print("reverse = ",new_list)



# ///////// string sorting //////////
words = ["teena","mega","jyoti"]
new_words = sorted(words,key=len)
print(new_words)

new_words_rev = sorted(words,reverse=True, key=len)
print(new_words_rev)
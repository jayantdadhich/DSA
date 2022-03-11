str1 = input("Enter the Sentence: ")
words = str1.split(".")           #returns a list
# print(words)
rev_words = words[::-1]
print(rev_words)
sen = ".".join(rev_words)
print(sen)

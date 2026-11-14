#print a letter in which name and date is replaced to the user

# letter = '''
# Dear <|name|> 
# your are selected!
# <|date|> '''

# print(letter.replace("<|name|>", "Arman").replace("<|date|>" ," 1 aug"))

letter = '''
Dear <|name|> 
your are selected!
<|date|> '''

name = input("Enter your name : ")
date = input("Enter the date : ")

print(letter.replace("<|name|>", name).replace("<|date|>" , date))

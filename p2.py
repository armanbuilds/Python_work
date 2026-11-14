word = "Donkey"

with open("D:\\PYTHON\\FILE IINPUT-OUTPUT\\practice set\\donkey.txt") as f :
    content = f.read()

contentNew = content.replace(word,"######") 

with open("D:\\PYTHON\\FILE IINPUT-OUTPUT\\practice set\\donkey.txt" , "w") as f :
    f.write(contentNew)


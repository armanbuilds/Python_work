words = ["Donkey" , "bad" , "ganda"]

with open("D:\\PYTHON\\FILE IINPUT-OUTPUT\\practice set\\donkey.txt") as f :
    content = f.read()

for word in words:
       content = content.replace(word,"#" * len(word)) 

with open("D:\\PYTHON\\FILE IINPUT-OUTPUT\\practice set\\donkey.txt" , "w") as f :
    f.write(content)


file = open("D:\\PYTHON\\FILE IINPUT-OUTPUT\\file.txt", "w+")

file.write("New content")

file.seek(0)

print(file.read())

file.close()
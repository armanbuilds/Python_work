import os

path = "D:/1st semester materiaLs/AICT"

contents = os.listdir(path)

print("Contents of the directory:")

for item in contents:
    print(item)
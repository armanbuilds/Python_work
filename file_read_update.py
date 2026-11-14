# r+ _ Read + Write
'''
1."r+" (Read and Write): Opens the file for both reading and writing. The file must already exist, or Python will throw an error.
'''


file = open("D:\\PYTHON\\FILE IINPUT-OUTPUT\\data.txt", "r+")

print(file.read())

file.write("\nI am learning file handling")

file.close()
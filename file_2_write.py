st = "He lives in hnd"

f = open("D:\\PYTHON\\FILE IINPUT-OUTPUT\\file.txt","+" )
f.write(st)
f.write("\n")
f.write("hello")
# if(f.write(st)):
#     print("saved")
f.close()


'''
r  for read mode

w for writing mode

a for append mode

+ for update
1."r+" (Read and Write): Opens the file for both reading and writing. The file must already exist, or Python will throw an error.

2."w+" (Write and Read): Opens the file for both reading and writing. Warning: This will completely overwrite/erase the existing file contents as soon as it opens.

3."a+" (Append and Read): Opens the file for both reading and writing. It will seamlessly add new data to the very end of the file without erasing anything.

rb for reading in binary

rt for reading in text form

'''
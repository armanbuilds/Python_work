name = "Arman"
#     A   R   M   A   N
#    (0)  (1)  (2)  (3)  (4)
#    (-5)  (-4)  (-3)  (-2)  (-1)

print(name[0],"\n")
print(name[1],"\n")
print(name[2],"\n")
print(name[3],"\n")
print(name[4],"\n")

#  name = name[1:2]     #this makes only r to store in name
# print(name)
print(name[1 : 4])  #start from 1 and end on 3 (3 included and 3 excluded)
print(name[-4 : -1]) #start from 1 and end on 3(3 included and 3 excluded)
print(name[ : 3])   #with no start poitn means start from 0
print(name[0:])   #with no end points mean end on length - 1(index[4] included)
print(name[::-1])   #print the string in reverse order
print("The length of",name,"is",len(name))   # to find the length of string
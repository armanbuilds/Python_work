#different operation on strings 

friends = ["ali" , "ahmad" , "mujeeb" , 123 , 23.4,False]

#1.
# print(friends[0] , friends[1])

#2.
# friends[0] = "bakr"    #changes the value at pointed index
# print(friends[0])

#3.
# print(friends)  #prints whole list

#4.
# friends.append(False)
# print(friends)      # adds new item to end of list

#5.
# friends.insert(0,"bakr")
# print(friends)          #inserts specific value at specific index and if that speific index causes to create space then it automatically fits at the end.
#insert(3,8) insert 8 at 3 index (index,value)

#6.
#SLICING OF LISTS LIKE STRING
# print(friends[1:4])

#7. returns the removed value
friends = [5, 2, 8, 1]
# friends.pop(3)
# print(friends)


# x = friends.pop(1)
# print(x)
# print(friends)
# print(friends.pop(2))   # IMP: both returns the  poped value 

#8.   Removes the first occurrence of a value.Value is given to the function not the index
# friends.remove(23.4)
# print(friends)

#9.
# friends = [5, 2, 8, 1]
# friends.sort()
# print(friends)
# print(friends.sort())  #return the value which is "none"

#10.
# friends = [5, 2, 8, 1]
# friends.reverse()
# print(friends)
# print(friends.reverse())  #return the value which is "none

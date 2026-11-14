#1  ADD
a = {1,2,3,4,}
# print(a.add(5))     #prints "none" bcz add() changes the original set directly, but it doesn't return the updated set.
# print(a)
# a.add(5)
# print(a)


#2   REMOVE
# Removes a specific element. if the element is not present it gives a key error 
# a.remove(4)
# print(a.remove(4))    #OUTOUT --> NONE 
# print(a)


#3   DISCARD
# It also removes an element, but there's an important difference from remove().
# a.discard(10)
# print(a.discard(4))    #OUTOUT --> NONE 
# print(a)


#4   CLEAR
# clear() — Remove everything
# a.clear()
# print(a)

#5   POP
# pop() — Remove a random element

# x = a.pop()     #it returns a poped element 
# print(x)    
# print(a)

#6 LENGTH
print(len(a))
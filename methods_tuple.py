#METHODS OF TUPLE 

#1.
# fruits = ("Apple","Banana","Orange")
# print("Apple" in fruits)      #membership operator checks that valur is present or not.

#2.
# numbers = (10,20,30)
# for i in numbers:    #loops in tuple
#     print(i)

#3.
# numbers = (1,2,3,2,2,5)   #counts the given value 
# x = numbers.count(2)    # or print(numbers.count(2))
# print(x)

#4.
# numbers = (10,20,30,20)
# print(numbers.index(20))   #Returns the first position of a value.

#5. SORTED
# numbers = (5,2,8,1)
# print(sorted(numbers))  #Notice that sorted() returns a list, not a tuple.

#6.  tuple -->  list
# t = (1,2,3)
# l = list(t)   #conversion of list into tuple 
# print(l)

#7.Concatenation (+)
# t1 = (1, 2, 3)
# t2 = (4, 5)
# result = t1 + t2
# print(result)


#8.Repetition (*)
# t = ("Hi",)
# print(t * 4)  

#OR   
# s = t*4
# print(s)

#9.Nested Tuple Access
student = (
    ("Ali", 20),
    ("Ahmed", 22),
    ("Sara", 19)
)
               # important concept 
print(student[1])
print(student[1][0])
print(student[2][1])

d = {}  #empty dictionary
marks = {
    "Name" : "Arman" ,
    "Age": 18,
    "Height" : "6ft",
    0 : "Ali"
}

#1  .items()
# print(marks["Name"])
# print(marks.items())   #Gives the items of dictionary in tuple form
# a = marks.items()
# print(a)   #possible becaus dictionary is mutable

#2    .keys() 
# It gives the keys of dictionary
# print(marks.keys())


#3
#2    .values() 
# It gives the values of dictionary
# print(marks.values())

#4    .update()
#update the value of dictioanry
# marks.update({"Age": 19 , "Ahmed " :20} )   #if the update key vlsue pair id not present it added then
# print(marks)


#5    .get()
# print(marks.get("Arman"))   #this prints none
# print(marks["Armanl"])    #this returns error


#6  pop()
#Removes a specific key and its value
# a = marks.pop("Age")       #returns the value of poped key
# print(a)
# print(marks)

#7   popitem()   Removes the last inserted key-value pair
# print(marks.popitem())
# a = marks.popitem()    #returns the poped value
# print(a)
# print(marks)

#8     clear()
#Removes all items.
print(marks.clear())    #it returns none
print(marks)   #it prints {} 
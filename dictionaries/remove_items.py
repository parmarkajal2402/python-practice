thisdict = {
    "name" : "kajal",
    "age" : 20,
    "address" : "rajkot"
}
thisdict.pop("age")
print(thisdict)

#The popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name
del thisdict["name"]
print(thisdict)

#The clear() method empties the dictionary
thisdict.clear()
print(thisdict)

#he del keyword can also delete the dictionary completely
del thisdict
print(thisdict) #it gives error because "thisdict" no longer exists.
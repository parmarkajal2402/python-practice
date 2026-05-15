thisdict = {
    "name" : "kajal",
    "age" : 20,
    "address" : "rajkot"
}
thisdict["year"]=2026
print(thisdict)

#The update() method will update the dictionary with the items from a given argument.
#If the item does not exist, the item will be added.
thisdict.update({"color" : "red"})
print(thisdict)

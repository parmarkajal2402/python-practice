thisdict = {
  "name": "kajal",
  "age": 20,
  "address": "rajkot"
}
x = thisdict["name"]
print(x)

y = thisdict.get("age")
print(y)

#The keys() method will return a list of all the keys in the dictionary.
z = thisdict.keys()
print(z)

#The values() method will return a list of all the values in the dictionary.
m = thisdict.values()
print(m)
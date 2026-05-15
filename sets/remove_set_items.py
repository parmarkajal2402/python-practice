fruits = {"apple", "banana", "cherry","mango"}
#Remove Method
fruits.remove("banana")

print(fruits)

#Discard Method
fruits.discard("cherry")

print(fruits)

#Remove a random item by using the pop() 
x = fruits.pop()

print(x)

print(fruits)

#The clear() method empties the set
fruits.clear()
print(fruits)

#del keyword will delete the set completely
del fruits
print(fruits)
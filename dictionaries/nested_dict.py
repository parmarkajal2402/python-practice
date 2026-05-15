#A dictionary can contain dictionaries, this is called nested dictionaries.
students = {
    "stud1" : {
    "sname1" : "kajal",
    "age" : 20
},
   "stud2" : {
    "sname2" : "shital",
    "age" : 19
},
  "stud3" : {
      "sname3" : "jensi",
      "age" : 12
  }
}
print(students)

#Another way
#Create three dictionaries, then create one dictionary that will contain the other three dictionaries
stud1 = {
    "sname1" : "kajal",
    "age" : 20
}

stud2 = {
    "sname2" : "shital",
    "age" : 19
}

stud3 = {
    "sname3" : "jensi",
      "age" : 12
}

students = {
    "stud1" : stud1,
    "stud2" : stud2,
    "stud3" : stud3
}

print(students)
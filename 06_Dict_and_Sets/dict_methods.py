marks = {
    "Sudhir": 100,
    "Suraj": 34,
    "raj": 344
}

# print(marks,type(marks))
print(marks.items()) # give all the items present in the dictionary along with the key value pairs.

print(marks.keys()) # it gives all the key present in the dictionary.

print(marks.values()) # it gives all the values present in the dictionary.

marks.update({"Sudhir": 323})
print(marks) # update the values in the dictionary.

print(marks.get("Sudhir"))
# get the values in the dictionary.

print(marks.get("Sudhir2")) # give the None if key value is not present.

print(marks["Sudhir3"]) # gives the error message.

# 2:39:51
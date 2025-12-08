# readline() function gives the single line from the given file.

# f = open("myFile.txt")
# line = f.readline()
# print(line)
# f.close()



# readlines() function gives the all the lines in a form of list.

f = open("myFile.txt")
line1 = f.readlines()
print(line1,type(line1))
f.close()
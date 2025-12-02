# break keyword is used to exit the loop right at that instance

# so in this ex the i goes upto the 16 and program gets stop.
for i in range(20):

    if(i == 17):
        break
    print(i)

# ----------------------

# continue keyword is used to skip the loop value right at that instance

# so in this ex the i goes upto the 16 and skip the 17 num and program gets completed.
for i in range(20):

    if(i == 17):
        continue
    print(i)
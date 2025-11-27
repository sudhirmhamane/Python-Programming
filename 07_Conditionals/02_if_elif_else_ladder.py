# if elif else ladder

'''
if elif else statements are a multiway decision taken by our program due to certain conditions in our code

'''

a = int(input("Enter your age: "))

if(a > 18):
    print("you are eligible for voting!")
    print("You can vote now")

elif(a < 0):
    print("Your are entering negative age, please enter valid age")

elif(a == 0):
    print("Your are entering 0 as age, please enter age grater than 0.")

else:
    print("you are under age")
    print("Not eligible for voting!")
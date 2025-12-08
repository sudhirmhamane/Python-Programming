import random
'''
snake, water and gun game with computer

1 for the snake
-1 for the water
0 for the gun

'''
computer = random.choice([-1, 0, 1])
yourStr = input("Enter your choice: ")
youDist = {"s": 1, "w": -1, "g": 0}
reverseDist = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDist[yourStr]

print(f"You choose: {reverseDist[you]} \nComputer choose: {reverseDist[computer]}")


if(computer == you):
    print("It's a Draw")

else:
    if(computer == -1 and you == 1):
        print("You Win!")
    elif(computer == -1 and you == 0):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("You Lose!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Lose!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    else:
        print("Something went wrong!")
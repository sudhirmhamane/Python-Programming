'''

A funtion is a group of statements performing a specific task.

when ta program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what!

A function can be reused by the programmer in a given program any number of.


Example and Syntax of a Function

the sytax of a function looks as follows: 

def func1():
    print("Hello")

for calling this function, we put the name of the function followed by parentheses as follows

func1() -> this is called a function call.


def avg():
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = int(input("Enter the number: "))

    avg =  (a+b+c) / 3

    print(avg)

avg()
avg()
avg()
avg()
avg()



name = input("enter your name: ")

def greet():
    print(f"good mooring, {name}")

greet()



# function with arguments

def hello(name, ending):
    print("hello",name)
    print(ending)


hello("sudhir", "thank you")

'''
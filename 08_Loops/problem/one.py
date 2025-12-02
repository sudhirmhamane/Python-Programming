'''
1.print table of given number from user using while loop

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")

---------------------

 2.print table of given number from user using while loop

i = 1
while(i <11):
    print(f"{n} X {i} = {n * i}")
    i += 1

-----------------

3. print names starting from 's' letter in given list.

l = ["Suraj", "Suman", "Raj", "Gharu"]

for name in l:
    if(name.startswith("H")):
        print(f"Hello {name}")
else:
    print("Name is not found!")
-----------------


4. check given number prime or not

n = int(input("Enter a number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
----------------

5. sum on first natural number

n = int(input("Enter the number: "))

i = 1
sum = 0

while(i <= n):
    sum+=i
    i+=1
print(sum)

''' 

# 6. factorial of given number

# n = int(input("Enter a number: "))
# product = 1
# for i in range(1,n+1):
#     product = product * i
# print(f"the factorial of {n} is {product}")


# star pattern

# n = int(input("Enter a num: "))

# for i in range(1,n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1), end="")
#     print("")


# n = int(input("Enter a num: "))

# for i in range(1,n+1):
#     print()
#     print("*" * (i), end="")
#     print("")



# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     if(i == 1 or i == n):
#         print("*" * n)
#     else:
#         print("*", end="")
#         print(" "* (n-2), end="")
#         print("*", end="")
#         print("")


# n = int(input("Enter the number: "))

# for i in range(1,11):
#     print(f"{n} X {11-i} = {n * (11-i)}")

a = int(input("Enter first num: "))
b = int(input("Enter sec num: "))
c = int(input("Enter third num: "))
d = int(input("Enter fourth num: "))

largest = max(a,b,c,d)

print("Largest value is: ",largest)


if(a>=b and a>=c and a>=d):
    print("A is largest")
elif(b>=a and b>=c and b>=d):
    print("B is largest")
elif(c>=a and c>=b and c>=d):
    print("C is largest")
else:
    print("D is largest")

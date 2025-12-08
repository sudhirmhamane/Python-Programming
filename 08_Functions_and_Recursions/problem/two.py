def c_to_f(c):
    return ((c/5)*9)+32

c = int(input("Enter a temperature in C: "))
f = c_to_f(c)
print(f"{round(f,2)} far")

# c/5 = f-32/9
# c = 5*(f-32)/9
# f = (c/5)*9+32
# sum of first n natural number using the recursion


'''

so how we can do sum in manual way

sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
.
.
.
sum(n) = sum(n-1) + n

'''

def sum(n):
    if(n == 1): # this is the bace case
        return 1
    return sum(n-1) + n

print(sum(5))
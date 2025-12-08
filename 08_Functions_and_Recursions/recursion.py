'''

Recursion — Short Notes

    Recursion is a process where a function calls itself to solve a problem.

    Every recursive process has two parts: a stopping condition and a repeating step.

    The stopping condition prevents infinite looping and tells the function when to end.

    The repeating step breaks the problem into a smaller or simpler version of itself.

    Recursion is useful for problems that naturally break into subproblems, such as tree structures, divide-and-conquer tasks, and backtracking.

    Recursive thinking focuses on solving a small part and letting the function handle the rest.

    Recursion can be elegant but may use more memory than iterative solutions because each call is stored on the call stack.

    A missing or incorrect stopping condition leads to infinite recursion and eventually an error.

    Python has a limit on how deeply recursion can go, so extremely deep recursive processes may require alternatives.

'''

def fact(n):
    if(n==1 or n==0):
        return 1
    return n * fact(n-1)

n = int(input("Enter a number: "))
print(f"the fact of {n} is: {fact(n)}")


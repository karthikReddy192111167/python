def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

def count(b):
    return fib(b+1)

b = int(input("Enter the number:"))
print("Number of ways:", count(b))

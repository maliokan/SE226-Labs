def factorial(x: int):
    if x == 0 or x==1:
        return 1
    return factorial(x-1)*x


abs_term = lambda x, i: (x**(2*i)) / factorial(2*i)


x = int(input("x: "))
n = int(input("n: "))

def exp_x(x: int , n: int):
    summmation = 0.0
    for i in range(n):
        summmation += (-1)**i * abs_term(x, i)
    return summmation

print(exp_x(x,n))

y = 0

def g(n, r):
    """this function takes parameter n and r then assigns
    the value to global variable y. returns nothing"""
    global y
    if n < 0:
        return
    y += r**n
    g(n - 1, r)


print(g.__doc__)
g(3,2)
print(y)
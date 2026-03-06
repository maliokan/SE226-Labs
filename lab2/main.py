print("Task 1!")
num = int(input("Please enter a positive integer greater than 9: "))

step = 0

print(str(num), end="")
while num > 9:
    print(" -> ", end="")
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    print(sum, end="")
    num = sum
    step += 1


print("\nFinal value:", num)
print("Total steps:", step)


print("\n\nTask 2!")
n = int(input("Please enter a number between 10 and 100: "))
while n < 10 or n > 100:
    n = int(input("Invalid input. Please enter a number between 10 and 100: "))


f = 0
b = 0
fb = 0

for i in range(1, n+1):
    if i % 7 == 0: continue
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fb += 1
    elif i % 3 == 0:
        print("Fizz")
        f += 1
    elif i % 5 == 0:
        print("Buzz")
        b += 1
    else:
        print(i)

print("--- Summary ---\n","Fizz count :", f, "\nBuzz count :", b , "\nFizzBuzz count:", fb)


print("\n\nTask 3!")

m = int(input("Please enter a number between 3 and 9:"))

for i in range(1, 2*m):
    k = m - abs(m - i)
    for j in range(1,k+1):
        print(j, end="")
    print()


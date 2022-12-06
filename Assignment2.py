# Check if A Number prime or not
"""
n = int(input("enter any number"))

flag = False

if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            flag = True
            break
if flag:
    print(n, "is not a prime number")
else:
    print(n, "is a prime number")
    """

# Use that function, and print first 100 prime number

s = 1
e = 100

if s > 0:
    count = 0
    for i in range(s, e+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                count += 1
                print(i)
else:
    print("Invalid Number")
print("\n Total", count)




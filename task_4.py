integer = int(input("Enter positive integer: "))
maximum = 0
n = integer
while n > 0:
    x = n % 10
    n = n // 10
    if x > maximum:
        maximum = x
    else:
        continue
print(maximum)

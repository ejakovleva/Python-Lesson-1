a = int(input("How many miles did you run the first time you started jogging? "))
b = int(input("How many miles do you want to run every day? "))

# while int(a) <= b:
#     print(f'{a:0.2f}')
#     a = a * 1.1
days = 1
while True:
    days += 1
    a = a * 1.1
    if int(a) == b:
        break
print(f"Taking into account your running pace you will reach {b} miles on the {days}th day.")

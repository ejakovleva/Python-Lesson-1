vehicle_type = "car"
car_model = "toyota rav4"
max_speed = 280
horsepower = 145
print(vehicle_type)
print(car_model)
print(max_speed)
print(horsepower)

age = int(input("What is your age? "))
if age >= 18:
    alcohol_type = input("What type of alcohol are you looking for? ")
    print(alcohol_type + " is a great choice. Today we have a special discount only for " + alcohol_type + ". "
          + "Go via the link and get 10% discount.")
else:
    print("The entrance is prohibited")



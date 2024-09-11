import os
os.system("cls")

name = input("Whats your name? ")
age = int(input("How old are you? "))
weeks = age * 52
print("Welcome ", name, " you have lived ", weeks, " weeks(=")

x = float(input("x: "))
y = float(input("y: "))

print(x + y)
print(x - y)
print(x * y)
print(x ** y)   #For example 5**3 = 5^3 = 125
print(x / y)
print(x // y)   #division without decimals
print(x % y)    #how much remains after the devision

weight = float(input("How much do you weigh in kg? "))
height = float(input("How tall are you in meters? "))
print(weight/height**2)

kg = float(input("How many kg to you want to convert to lb? "))
print(kg*2.205, "lbs")
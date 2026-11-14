#DAILY DSA ON PYTHON
#day 1

#1 Write a Python program that accepts your name, age and college name and prints them.

name = input("Enter Name :  ")
age = int(input("Enter Age  "))
cname = input ("Enter college Name :    ")


print(f"\n\nName : {name}\nAge : {age}\nCollege Name : {cname}")

#2 Accept two integers and print their sum.

a= int(input("Enter First Number :  "))
b = int(input("Enter Second Number :    "))

add = a+b

print(f"SUm of Two Integers are : {add}")

#Q3. Swap Two Numbers
#Swap two numbers using a third variable.
a= 10 
b =20

c=a
a=b
b=c

print (a)
print(b)

#Q4. Calculate Area of a Rectangle
#Accept length and breadth and calculate the area.
l =int(input ("Enter lenght :   "))
b =int(input ("Enter Bredth :   "))

a = l*b
print(f"\nAREA OF RECTANGLE : {a}")

#Convert Celsius to Fahrenheit
#Accept temperature in Celsius and convert it into Fahrenheit.
#F = (°C × 9/5) + 32

c= int(input("Enter Temp in celsius : "))
f = (c*(9/5))+32

print(f" Celsius to Fahrenheit : {f}f")

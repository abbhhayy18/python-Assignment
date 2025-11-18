#Write a Python program to display calendar?
import calendar
year=int(input("enter the year :"))
month=int(input("enter the month :"))
print(calendar.month(year,month)) # only 11th month calendar
print(calendar.calendar(year)) # whole year calendar

#Write a Python program to convert Celsius to Fahrenheit?
celsius=int(input("Enter the celsius :"))
fahrenheit=celsius*33.8
print(f"In {celsius}°C there are {fahrenheit}°F")

#Write a Python program to solve quadratic equation?
# (-b+ under_sqr_root b sqr-4ac)/2a
# (-b+ under_sqr_root b sqr-4ac)/2a
import cmath
a=float(input("Enter the value of a "))
b=float(input("Enter the value of b "))
c=float(input("Enter the value of c "))
d= (b**2) - (4*a*c)
root1= (-b+cmath.sqrt(d))/(2*a)
root2= (-b-cmath.sqrt(d))/(2*a)
print(f"roots of quadratic equation are{root1} and {root2}")

# Write a Python program to swap two variables without temp variable?
a=10
b=20
a,b=b,a 
print(f"a={a}")
print(f"b={b}")

#Write a Python program to convert kilometers to miles?
kilometer=int(input("enter the kilometer :"))
miles=kilometer*0.621371
print(f" In {kilometer} kilometer there are {miles} miles")

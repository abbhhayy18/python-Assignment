#Q1 calculate electric bill
unit=int(input("enter the amount of unit :"))
print("the bill of electricity is",end=" ")
if unit<100:
    print("0 rs")
if unit>100 and unit<200:
    print(unit*5,end="rs")
if unit>200:
    print(unit*5,end="rs")

#Q2 WAP to accept percentage from user and display the grade acc to the following criteria
percent_marks=int(input("enter the percentage:"))
print("you got grade",end=" ")
if percent_marks>90:
   print("A")
elif percent_marks>80 and percent_marks<=90:
   print("B")
if percent_marks>=60 and percent_marks<=80:
   print("C")
elif percent_marks<60:
   print("D") 
    
#Q3accept the age of 4 people and display the youngest one
print("enter the age of 4 people:")
age1=int(input("1st age:"))
age2=int(input("2nd age:"))
age3=int(input("3rd age:"))
age4=int(input("4th age:"))
if age1<age2 and age1<age3 and age1<age4:
    print(f"the youngest people is {age1} year old")
elif age2<age1 and age2<age3 and age2<age4:
     print(f"the youngest people is {age2} year old")
if age3<age2 and age3<age1 and age3<age4:
     print(f"the youngest people is {age3} year old")
elif age4<age2 and age4<age3 and age4<age1:
     print(f"the youngest people is {age4} year old")

#Q4 A company decided to give bonus to employee according to following criteria:
time_period=int(input("enter the time pwriods in digit:"))
salary=int(input("enter ur salary in digit:"))
print("your net bonous amount is: ",end="")
if time_period>10:
    print(salary*0.1)
elif time_period>=6 and time_period<=10:
    print(salary*0.08)
if time_period<6:
      print(salary*0.05)

#Q5Accept three numbers from the user and display the second largest number?
print("enter three numbers")
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))
if (num2 <num1 <num3) and (nu3 <num1 <num2):
    print(num1)
elif (num1 <num2 <num3) and (num3 <num2 <num1):
    print(f"second largest number is {num2}")
if (num2 <num3 <num1) and (num1 <num3 <num2):
    print(f"second largest number is {num3}")

#Q6Accept the marked price from the user and calculate the Net amount as (Marked Price – Discount) to pay according to following criteria:
marked_price=int(input("enter marked price:"))
print("your net amoumt to be paid is ",end="")
if marked_price>10000:
    print(int(marked_price-(marked_price*0.2)))
elif marked_price>7000 and marked_price<=10000:
    print(int(marked_price-(marked_price*0.15)))
if marked_price<=7000:
    print(int(marked_price-(marked_price*0.1)))

#Q7 Accept the marks of English, Math and Science,Social Studies Subject and display the stream allotted according to following:
#All Subjects more than 80 marks — Science Stream
#English >80 and Math, Science above 50 — Commerce Stream
#English > 80 and social studies > 80 — Humanities

print("enter the marks of subjects")
english=int(input("enter english marks:"))
maths=int(input("entescience marks:"))
science=int(input("enter science marks:"))
social=int(input("enter social marks:"))
if (english>80 and science>80):
    print("you should go for science stream")
elif english >80 and maths>50 and science>50:
      print("you should go for commerce stream")
if english > 80 and social> 80:
    print("you should go for humanities")
elif social>80 and maths>80:
    print("you should go for science stream")

#Q8. Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye"?
user_input=int(input("input any number:"))
if user_input % 5==0:
    print("hello")
else:
    print("bye")

#Q9. Write a program to check whether the last digit of a number(entered by user) is divisible by 3 or not?

num_1=int(input("enter number:"))
last_digit=num_1%10
if last_digit % 3==0:
    print("it is divisible by 3")
else:
    print("it is not dividible by 3")

#Q10. Write a program to check whether a number entered is three-digit number or not?
user_choice=int(input("enter the number "))
if user_choice>=100 and user_choice<=999:
    print("it is three digit number")
else:
    print("it is not three digit number")



#Question 1: Write a Python program to print all the numbers from 1 to 10 using a for loop.
for num in range(1,11):
    print(num,end=" ")
print(end="\n")

#Question 2: Write a Python program to find the sum of all numbers from 1 to 100 using a for loop.
sum=0
for num in range(1,101):
    sum+=num
print(sum)

#Question 3: Write a Python program to print the multiplication table of a given number using a for loop.
num=int(input("enter any number:"))
for i in range(1,11):
    print(num*i)

#Question 4: Write a Python program to count the number of even and odd numbers from a series of numbers using a for loop.
list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count=0
count1=0
for item in list1:
    if item % 2 ==0:
        count+=1
    else:
        count1+=1
print(f"even numbers are {count} and odd numbers are {count1}")

#Question 5: Write a Python program to find the factorial of a number using a for loop.
num=int(input("enter the number for factorial:"))
factorial=1
for i in range(1,num+1):
    factorial*=i
print(f"factorial of {num} is {factorial}")

#Question 6: Write a Python program to print the Fibonacci sequence up to a specified number using a for loop.
num=int(input("enter any num: "))
list1=[]
for i in range(num):
    if i<=1:
        list1.append(i)
    if i>1:
        list1.append(list1[i-1]+list1[i-2])
for i in list1:
    print(i,end=" ")
    print(end="\n")

#Question 7: Write a Python program to check if a given number is prime or not using a for loop.
num = int(input("enter number to check prime: "))
for n in range(4,num):
    if num <= 1:
        print(f"{num} is not prime number")
        break
    if num==2 or num==3:
        print(f"{num} is a prime number")
        break
    if num % 2 ==0 or num % 3 ==0:
        print(f"{num} is not prime number")
        break
    if num>3 and num % n!=0:
        print(f"{num} is a prime number")
        break
    elif num>3 and num%n==0:
        print(f"{num} is not prime number")
        break
    print(end="\n")

#Question 8: Write a Python program to find the largest element in a list using a for loop.
list1=[8,1,4,6,3,9,5]
for i in range(len(list1)):
    for j in range(len(list1)-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print("largest element of list is ",list1[-1])

#Question 9: Write a Python program to reverse a given string using a for loop.
str="python"
str2=""
for i in str:
    str2=i+str2
print(str2)

#Question 10: Write a Python program to find the common elements between two lists using a for loop.
#List1 = [1,2,3]
#List2 = [4,5,1] # common element is 1
list1 = [1,2,3]
list2 = [4,5,1]
print("common element is ",end="")
for i in list1:
    if i in list2:
        print(i)



    
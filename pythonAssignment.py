#Q1.concatenate two string
str1="hello"
str2="world"
print(str1+" "+str2) # output:hello world

#Q2.using + operator
str1="hello"
str2="world"
print(str1+" "+str2) # output:hello world

#using join() method
list1=["hello","world"]
result=" ".join(list1)
print(result) #output:hello world

#Q3.access individual character in strings
text="i love to learn python"
for item in range(len(text)):
    print(text[item],end=" ")

#Q4 method to find length of string
text="i am learnig python"
len_of_str=len(text)
print(len_of_str)

#Q5 converting string into upper case
text="hello world"
print(text.upper())

#Q6 converting string into lower case
text="HELLO WORLD"
print(text.lower())

#Q7 method to replace substring from string
text="i am learning python"
print(text.replace("python","java"))

#2nd method for replacing substring
text="hello world"
result=text.maketrans("hel","xyz")
print(text.translate(result))

#Q8 split string using delimeter
text="i-am-learning-python"
print(text.split("-"))

#Q9 check if a string starts with particular substring
text="python programming"
print(text.startswith("pyt")) #output:true

#Q10 check if a string ends with particular substring
text="python programming"
print(text.endswith("ing")) #output:true

#Q11 removing leading and trailing space feom string
text="  hello world  "
print(text.strip(" "))

#Q12 finding index of first occurance of a substring
text="python programming"
print(text.find("pr"))

#Q13 count number of occurance of substings
text="all animals are amazing and adorable"
print(text.count("a"))

#Q14 check if string contains only alphabetic character
text="python"
print(text.isalpha())

#Q15 check if string contains only numeric character
text="865199"
print(text.isnumeric())

#Q16 how can u check if string is palindrome
text="1234321"
reverse_text = text[::-1]
if text == reverse_text:
    print("it\'s palindrome")
else:
    print("not palindrome")

#Q17 reverse string
text="programming"
print(text[::-1])

#Q18 format string using placeholders for variable values
name="abhay"
age="23"
city="noida"
print(f"My name is {name} i am {age} years old and i live in {city}")

#Q19 access substring from string using slicing
text="characters"
sub_string=text[2:7:1]
print(sub_string)

#Q20 remove specific character from string
text="python programming"
print(text.replace("p","",1))
# Reverse string without built in function 
"""str1='123456789'
str2=''
for item in str1:
    str2=item+str2
print(str2)"""

def reverse_str(str_val:str)->str: # it tells programmer that it accept string valu and return to make it more readability
    """ not isintance() is a method to check the value is string or not"""
    if not isinstance(str_val,str):
        raise TypeError("its not string value")

    """reversing the string using for loop by adding character before previous one """

    reverse_string=""
    for i in str_val:
       reverse_string=i+reverse_string
    return reverse_string

""" __name__ is a built in variable that value inside current file is __main__"""
if __name__== "__main__":
    try:
        str_val=input("enter th string :")
        result=reverse_str(str_val)
        print(result)
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)


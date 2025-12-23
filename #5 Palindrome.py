# Palindrome check
def palindrome(str1:str)->str:
    # if user input in not string value raise error
    if not isinstance(str1,str):
        raise ValueError("Value Error :enter value again")
        
    # Creating empty string to store reverse user input
    str2=""
    for i in str1:
        str2=i+str2
    #if reverse user input is equal to original user input return true
    if str2==str1:
        return True
    # if not thn return false
    else:
        return False
if __name__ == "__main__":
    try:
        # Taking input from user
        str1=input("enter the value to check the palindrome :")
        if palindrome(str1):
            print(f"{str1} is Palindrome")
        else:
            print(f"{str1} is not palindrome")
    except ValueError as ve:
        print(ve)
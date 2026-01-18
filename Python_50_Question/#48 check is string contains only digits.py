"""  Check if String Contains Only Digits  
● Write a function that checks if a string contains only numeric characters.  
Example:  
● Input:  
string = "123456"  
● Expected Output:  
True  
● Input:  
string = "123a56" 
● Expected Output:False """
class ONLY_DIGITS:
    def only_digits(self,str1):
        if str1.isdigit():
            return True
        else:
            return False

if __name__ == "__main__":
    str1 = input("ENTER the string:")
    obj = ONLY_DIGITS()
    print(obj.only_digits(str1))
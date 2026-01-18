""" Check if Number is Armstrong Number  
● Write a function that checks if a number is an Armstrong number.  
● Example: 153 is an Armstrong number  
because 13+53+33=153. """
class ARMSTRONG:
    def armstrong(self,num):
        result=0
        if num.isdigit():
            for item in num:
                result+=int(item)**3
            if result == int(num):
                return True
            else:
                return False
        else:
            raise ValueError

if __name__ == "__main__":
    try:
        num=input("Enter the number to check armstrong:")
        obj = ARMSTRONG()
        print(obj.armstrong(num))
    except ValueError:
        print("ERROR: Enter digits onlt->")

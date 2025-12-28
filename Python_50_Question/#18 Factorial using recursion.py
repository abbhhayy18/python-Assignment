"""Factorial Using Recursion  
● Write a recursive function to calculate the factorial of a given number.  
● Example  
Input: n = 5  
Expected Output: 120 (since 5*4*3*2*1=120)"""
class FACTORIAL:
    def factorial(self,num):
        try:
            num=int(num)
        except:
            raise ValueError("ERROR:Enter only digits as input>>>>")
        if num == 1:
            return 1
        return num*self.factorial(num-1)

if __name__ == "__main__":
    try:
        num=input("Enter the number for factorial:")
        obj = FACTORIAL()
        print(obj.factorial(num))
    except ValueError as error:
        print(error)
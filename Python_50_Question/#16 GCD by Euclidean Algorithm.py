# Calculate GCD Using Euclidean Algorithm  
"""Input: a = 48, b = 18  
Expected Output: 6 (the GCD of 48 and 18 is 6)"""
class GCD:
    def gcd(self,num1,num2):
        try:
            num1=int(num1)
            num2=int(num2)
        except:
            raise ValueError("ERROR:Enter only digits...")
        while(num2 > 0):
            # num1 will become num2 and num2 will become reminder of num1 and num2
            num1,num2 = num2,num1 % num2
        return num1
            
if __name__ == "__main__":
    try:
        num1=input("Enter the first number:")
        num2=input("Enter the second number:")
        obj = GCD()
        print(f"The Greatest Common Divisor of {num1} and {num2} is ",obj.gcd(num1,num2))
    except ValueError as error:
        print(error)
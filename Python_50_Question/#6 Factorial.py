# Factorial
class FACTORIAL:
    def factorial(self,num):
        try:
            num=int(num)
        except:
            raise ValueError("ERROR:Enter only integer digits")
        # If num is smaller thn or equal to 0 raise error
        if num <=0:
            raise ValueError("ERROR:Factorial is not defined for value 0 and negative integer")
        # declaring a variable(result) with value 1
        result=1
        for i in range(1,num+1):
            # Multiplying i with result and store in result
            result*=i
        return result

if __name__ == "__main__":
    try:
        # Taking input from the user
        num=input("enter the number :")
        obj = FACTORIAL()
        print(f"fatorial of {num} is",obj.factorial(num))
    except ValueError as ve:
        print(ve)
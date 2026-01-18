"""Check if a Number is a Power of 2  
● Write a function that checks if a given number is a power of 2.  
● Example:  
Input: 16  
Expected Output: True  
(Explanation: 24=16)  """

class POWER_OF_2:
    def __init__(self,num):
        try:
            self.num=int(num)
        except:
            raise ValueError("ERROR:Enter only digits")

    def power_of_2(self):
        while self.num > 0:
            if self.num % 2 != 0:
                return False
            self.num //= 2
            if self.num == 1:
                return True
        
if __name__ == "__main__":
    try:
        num=input("Enter the number:")
        obj = POWER_OF_2(num)
        print(obj.power_of_2())
    except ValueError as error:
        print(error)
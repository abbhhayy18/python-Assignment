"""Calculate Sum of Squares of First n Natural Numbers  
● Write a function to calculate the sum of squares of the first n natural numbers.  
● Example:  
Input: n = 3  
Expected Output: 14  
(Calculation: 1**2 + 2**2 + 3**2 =14) """
class SUM_OF_SQUARES:
    @classmethod
    def sum_of_squares(cls,num):
        try:
            num=int(num)
        except:
            raise ValueError("ERROR:Enter digits only->")
        sum1=0
        for i in range(num+1):
            sum1+=i**2
        return sum1

    
if __name__ =="__main__":
    try:
        num=input("Enter the number:")
        result = SUM_OF_SQUARES.sum_of_squares(num)
        print(result)

    except ValueError as error:
        print(error)

""". Reverse Integer  
● Write a function that takes an integer and returns its digits reversed.  
● Example:  
Input: 12345  
Expected Output: 54321  
● Example:  
Input: -6789  
Expected Output: -9876 """
class REVERSE_INTEGER:
    @classmethod
    def reverse_integer(cls,number):
        try:
            number=int(number)
        except:
            raise ValueError("ERROR:Enter digits only")
        num=int(number)
        str1=""
        if num < 0:
            num=abs(num) # abs convert -ve value to positive
            while num > 0:
                last =num % 10
                str1+= str(last)
                num = num // 10
            print("-"+str1)
        else:
             while num > 0:
                last =num % 10
                str1+= str(last)
                num = num // 10
             print(str1)


if __name__ == "__main__":
    try:
        number=input("Enter the number:")
        REVERSE_INTEGER.reverse_integer(number)
    except ValueError as error:
        print(error)
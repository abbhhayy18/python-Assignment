"""Convert Decimal to Binary  
● Write a function to convert a given decimal number to its binary representation.  
● Example  
Input: decimal = 10  
Expected Output: 1010 (the binary representation of 10 is 1010) """
class DECIMAL_TO_BINARY:
    def decimal_to_binary(self,num):
        try:
            num=int(num)
        except:
            raise ValueError("ERROR:Enter onli digits...")

        str1=""
        while num > 0:
            quotient=num //2
            reminder=num % 2
            str1=str(reminder)+str1
            num = quotient
        print(str1)

if __name__ =="__main__":
    try:
        num=input("Enter the number to convert into binary:")
        obj = DECIMAL_TO_BINARY()
        obj.decimal_to_binary(num)
    except ValueError as error:
        print(error)
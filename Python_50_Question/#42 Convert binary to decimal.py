"""Convert Binary to Decimal  
● Write a function to convert a binary number (as a string) to a decimal. 
Example:  
● Input:  
"1011"  
Expected Output:  11 """
class BINARY_TO_DECIMAL:
    def binary_to_decimal(self,binary):
        try:
            binary = int(binary)
        except:
            raise ValueError("ERROR:Enter binary number->")
        sums=0
        length = len(str(binary))-1
        for i in str(binary):
            sums+=int(i)*2**(length)
            length-=1

        print(sums)
        
if __name__ =="__main__":
    try:
        binary = input("Enter the binary number:")
        obj = BINARY_TO_DECIMAL()
        obj.binary_to_decimal(binary)
    except ValueError as error:
        print(error)
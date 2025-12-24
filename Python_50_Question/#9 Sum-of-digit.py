# Sum of digit
class SUM_OF_DIGIT:
    def sum_of_digit(self,integer):
        if integer.isdigit():
            sumof=0
            for i in integer:
                sumof+=int(i)
            print(f"the sum of digit is:",sumof)
        else:
            raise ValueError("ERROR: Enter the integer value only")
         
if __name__ =="__main__":
    try:
        integer=input("Enter the digit for sum : ")
        obj = SUM_OF_DIGIT()
        obj.sum_of_digit(integer)
    except ValueError as ve:
        print(ve)

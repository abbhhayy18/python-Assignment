#check wheather number is prime or not
# Example 13 is prime number
class PRIME_NUM:
    def __init__(self,num):
        pass
        
    def prime_num(self,num)-> bool: # here func catch object as self and num as num
        try:
            num=int(num)
        except:
            raise TypeError("ERROR:Enter only digit")
        if num <2:
            return False

        for i in range(2,num):
            if num % i == 0:
                return False
        else:
            return True    
if __name__ == "__main__":
    try:
        num=input("Enter the num:")
        obj = PRIME_NUM(num)
        if obj.prime_num(num):# here object pass itself and num pass
            print("it is prime number")
        else:
            print("it is not prime number")
    except TypeError as error:
        print(error)   

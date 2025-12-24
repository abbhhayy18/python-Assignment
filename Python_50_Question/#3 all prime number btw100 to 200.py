# Find the prime number between 100 to 200
class PRIME_NUM_BTW:
    def __init__(self):
        pass

    def prime_num(self,n1,n2):
        if not isinstance(n1,int) or not isinstance(n2,int):
            raise ValueError # when raise line execute it jumps to except block """

        print(f"you entered {n1} and {n2}" )

        for i in range(n1,n2):
            prime_n=True
            for j in range(2,i-1):
                if i % j==0:
                    prime_n=False
                    break
            if prime_n:
                print(i,end=" ")
            
if __name__ == "__main__":

    try:
        num1=int(input('enter the 1st number :'))
        num2=int(input('enter the 2nd number :'))
        obj = PRIME_NUM_BTW()
        obj.prime_num(num1,num2)
    except ValueError:
        print(' ERROR: Plese enter only integer values ')


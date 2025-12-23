# Find the prime number between 100 to 200
def prime_num(n1,n2):
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
            print(i)
            
if __name__ == "__main__":

    try:
        num1=int(input('enter the 1st number :'))
        num2=int(input('enter the 2nd number :'))
        prime_num(num1,num2)
    except ValueError:
        print(' ERROR: Plese enter only integer values ')


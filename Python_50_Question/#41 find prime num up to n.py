""" Generate a List of Prime Numbers Using Sieve of Eratosthenes  
● Write a function to generate all prime numbers up to a given number using the Sieve of 
Eratosthenes.  
Example:  
● Input:  
n = 20  
Expected Output:  
[2, 3, 5, 7, 11, 13, 17, 19]  """

class PRIME_NUM:
    def prime_num(self,num):
        try:
            num = int(num)
        except:
            raise TypeError

        if num < 2:
            raise TypeError 
        else:
            for item in range(2,num):
                is_prime = True
                for j in range(2,item):
                    if item % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(item,end=",")

if __name__ == "__main__":
    try:
        num = input("Enter the number for prime :")
        obj = PRIME_NUM()
        obj.prime_num(num)
    except TypeError:
        print(("ERROR: Invalid input!:Enter only digits and greater than 2"))
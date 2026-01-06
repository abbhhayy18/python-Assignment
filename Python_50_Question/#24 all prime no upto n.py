""" Find All Prime Numbers up to n  
● Write a function that returns a list of all prime numbers up to a given number n.  
● Example:  
Input: n = 10  
Expected Output: [2, 3, 5, 7] """
class PRIME_NO:
    def prime_num(self,num):
        try:
            num=int(num)
        except:
            raise ValueError("ERROR:Enter only digits as number-->")
        list1=[]
        for item in range(2,num):
            its_prime = True
            for i in range(2,item):
                if item % i==0:
                    its_prime = False
                    break
            if its_prime:
                list1.append(item)
        return list1

            
if __name__ == "__main__":
    try:
        num=input("Enter the number upto:")
        obj = PRIME_NO()
        print(f"ALL PRIME NUMBER UPTO {num} is->",obj.prime_num(num))
    except ValueError as error:
        print(error)
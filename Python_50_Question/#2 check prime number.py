#check wheather number is prime or not
# Example 13 is prime number
def prime_num(num):
    try:
        num=int(num)
    except:
        raise ValueError("ERROR:Enter only intger value")
    if num <=1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 ==0 or num % 3 == 0:
        return False
    if num > 3:
        for i in range(4,num):
            if num % i ==0:
                return False
        else:
            return True

if __name__ == "__main__":
    try:
        num=input("Enter the number to check the prime number:")
        if prime_num(num):
            print(f"{num} is prime number")
        else:
            print(f"{num} is not prime number")
    except ValueError as error:
        print(error)
# Create a function that generates a list of even numbers up to a given number
"""example 
   input : n =10
   output:[2,4,6,8,10]"""
class LIST_OF_EVEN:
    def list_of_even(self,num,list1)->list:
        try:
            num=int(num)
        except:
            raise ValueError("ERROR:Enter only digits") 
        for item in range(1,num+1):
            if item % 2 == 0:
                list1.append(item)
        return list1

if __name__ == "__main__":
    try:
        list1=[]
        num=input("Enter the number of even number:")
        obj = LIST_OF_EVEN()
        print(obj.list_of_even(num,list1))
    except ValueError as error:
        print(error)
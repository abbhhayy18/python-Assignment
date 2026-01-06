"""Calculate Sum of a List of Numbers Using Recursion  
● Write a recursive function to calculate the sum of a list of numbers.  
● Example:  
Input: [1, 2, 3, 4, 5]  
Expected Output: 15 """
class SUM_OF_LIST:
    def sum_of_list(self,list1,num):
        if num < 0:
            return 0
        return int(list1[num]) + self.sum_of_list(list1,num-1)

if __name__ == "__main__":
    try:
        list1=input("enter the list:").split()
        num = len(list1)-1
        for item in list1:
            if not item.isdigit():
                raise ValueError("ERROR:Enter only digits as element in list")
        obj = SUM_OF_LIST()
        print(obj.sum_of_list(list1,num))
    except ValueError as error:
        print(error)


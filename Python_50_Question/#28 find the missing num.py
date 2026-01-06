""" Find Missing Number in Consecutive List  
● Write a function to find the missing number in a list of consecutive numbers.  
● Example:  
Input: [1, 2, 3, 5, 6]  
Expected Output: 4 """

class MISSING_NUM:
    @staticmethod
    def missing_num(list1):
        for item in list1:
            if not item.isdigit():
                raise ValueError("ERROR:Enter th list with digits only-->")
        list2=[]
        for i in list1:
            list2.append(int(i))
        list2.sort()
        for item in range(len(list2)-1):
            if list2[item]+1 != list2[item+1]:
                print("The missing item is:",list2[item]+1)
                break
        else:
            print("No missing item found")



if __name__ == "__main__":
    try:
        list1=input("Enter the consecutive list with missing num:").split()
        obj = MISSING_NUM()
        obj.missing_num(list1)
    except ValueError as error:
        print(error)
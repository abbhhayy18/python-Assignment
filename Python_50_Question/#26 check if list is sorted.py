""" 26. Check if List is Sorted  
● Write a function that checks if a list is sorted in ascending order.  
● Example:  
Input: [1, 2, 3, 4, 5]  
Expected Output: True  """
class CHECK_SORTED_LIST:
    def check_sorted_list(self,list1):
        list2=sorted(list1)
        if list1 == list2:
            print("list is sorted")
        else:
            print("list is not sorted")
if __name__ == "__main__":
    try:
        list1=input("Enter the List:").split()
        obj = CHECK_SORTED_LIST()
        obj.check_sorted_list(list1)
    except ValueError as error:
        print(error)
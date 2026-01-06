"""Merge Two Sorted Lists  
● Write a function to merge two sorted lists into a single sorted list.  
● Example:  
Input: list1 = [1, 3, 5], list2 = [2, 4, 6]  
Expected Output: [1, 2, 3, 4, 5, 6]   """
class MERGE_SORTED_LIST:
    def merge_sorted_list(self,list1,list2):
        list3=list1+list2
        list3.sort()
        return list3

if __name__ =="__main__":
    try:
        list1=input("Enter the list1:").split()
        list2=input("Enter the list2:").split()
        obj = MERGE_SORTED_LIST()
        print(obj.merge_sorted_list(list1,list2))
    except ValueError as error:
        print(error)
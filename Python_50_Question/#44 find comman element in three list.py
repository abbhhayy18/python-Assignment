"""Find Common Elements in Three Lists  
● Write a function to find elements common in three lists.  
Example:  
● Input:  
list1 = [1, 2, 3, 4, 5]  
list2 = [3, 4, 5, 6, 7]  
list3 = [5, 6, 7, 8, 9]  
● Expected Output:  
[5]  """
class COMMON_ELEMENTS:
    def common_elements(self,list1,list2,list3):
        count =0
        for i in list1:
            if i in list2 and i in list3:
                print(i)
                count+=1
        if count == 0:
            print("There no common elements in all three lists")
        

if __name__ == "__main__":
    list1 = input("ENTER THE list1:").split()
    list2 = input("ENTER THE list2:").split()
    list3 = input("ENTER THE list3:").split()
    obj = COMMON_ELEMENTS()
    obj.common_elements(list1,list2,list3)
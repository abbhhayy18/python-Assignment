"""Find Largest Element in a List Using for Loop  
● Write a function to find the largest element in a list without using built-in max functions.  
● Example  
Input: [3,5,7,2,8,1]  
Expected Output: 8 (the largest element in the list is 8)"""
class LARGEST_ELEMENT:
    def largest_element(self,list1):
        for item in list1:
            if item.isdigit() or "." in item:
                pass
            else:
                raise ValueError("ERROR:Enter the digits only:")
        for i in list1:
            for item in range(len(list1)-1):
                if list1[int(item)] > list1[int(item+1)]:
                    list1[int(item)],list1[int(item+1)]=list1[int(item+1)],list1[int(item)]

        print(f"sorted list are :-->{list1}")
        print(list1[-1])

if __name__ == "__main__":
    try:
        list1=input("Enter the element of list:").split()
        obj = LARGEST_ELEMENT()
        obj.largest_element(list1)
    except ValueError as error:
        print(error)
""" Find the Median of a List of Numbers  
● Write a function to calculate the median of a list of numbers.  
Example:  
● Input:  
[1, 3, 5, 7, 9]  
Expected Output:  
5   """

class MEDIAN:
    def median(self,list2):
        list1=[]
        for item in list2:
            if not item.isdigit():
                raise ValueError
            else:
                list1.append(int(item))

        if len(list1) % 2 !=0:
            mid_value=len(list1)//2
            print(f"median is {list1[mid_value]}")
        else:
            value=len(list1)//2
            mid_value=(list1[value]+list1[value-1])/2
            print(f"median is {mid_value}")

if __name__ == "__main__":
    try:
        list2 = input("Enter the list:").split()
        obj = MEDIAN()
        obj.median(list2)
    except ValueError:
        print("ERROR:Enter digits only in the list->")

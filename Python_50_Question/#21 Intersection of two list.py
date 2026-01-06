"""Find Intersection of Two Lists  
● Write a function that returns the intersection of two lists without using set operations.  
● Example:  
Input: list1 = [1, 2, 3, 4, 5], list2 = [4, 5, 6, 7, 8]  
Expected Output: [4, 5]  """

class INTERSECTION_OF_LIST:
    def intersection_of_list(self,list1,list2)->list:
        list3=[]
        for item in list1:
            if item in list2:
                list3.append(item)
        return list3

if __name__ == "__main__":
    try:
        list1=input("Enter the 1st list:").split()
        list2=input("Emter the 2nd list:").split()
        obj = INTERSECTION_OF_LIST()
        print("The common element in both the list are-->",obj.intersection_of_list(list1,list2))

    except ValueError as error:
        print(error)
#Input: [7, 5, 8, 2, 10, 9]  
#Expected Output: 9
class SECOND_LARGEST:
    def sec_largest(self,list1):
        for item in list1:
            if not item.isdigit():
                raise ValueError("ERROR:Enter only digit as element")
        list2=[]
        for item in list1:
            list2.append(int(item))
        list2.sort()
        print(f"The second largest number in {list1} is:",list2[-2])

if __name__ == "__main__":
    try:
        list1=input("Enter the list :").split()
        obj =  SECOND_LARGEST()
        obj.sec_largest(list1)
    except ValueError as ve:
        print(ve)
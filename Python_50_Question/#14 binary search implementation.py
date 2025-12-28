"""
Binary search implementatin
Example  
Input: sorted_list = [1, 2, 3, 4, 5, 6] target = 4  
Expected Output: 3 (since 4 is at index 3) """
class BINARY_SEARCH:
    def __init__(self,list1,target):
        self.list1=list1
        self.target=target

    def binary_search(self):
        try:
            target=int(self.target)
        except:
            raise ValueError("ERROR:Enter only digits as Target")
        for item in self.list1:
            if not item.isdigit():
                raise ValueError("ERROR:Enter only digits as element in list")
            
        left = 0
        right =len(list1)-1
        while(left<=right):
            mid=(right+left)//2
            if target == int(list1[mid]):
                return mid
            elif target < int(list1[mid]):
                right=mid-1
            else:
                left=mid+1
        return "Target element are not found"

if __name__ == "__main__":
    try:
        list1=sorted(input("Enter the sorted list in digits:").split())
        print(list1)
        target=input("Enter the target element:")
        obj = BINARY_SEARCH(list1,target)
        result=obj.binary_search()
        print("index of terget element is ",result)
    except ValueError as error:
        print(error)
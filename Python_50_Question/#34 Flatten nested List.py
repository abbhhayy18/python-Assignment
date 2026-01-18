"""  Flatten a Nested List  
● Write a function to flatten a list that contains nested lists of integers.  
● Example:  
Input: [1, [2, [3, 4], 5], 6]  
Expected Output: [1, 2, 3, 4, 5, 6] """

class FLATTEN_NESTED_LIST:
    def flatten_nested_list(self,list1):
        list2=[]
        while len(list1) > 0:
            item = list1.pop(0)
            if isinstance (item,int):
                list2.append(item)
            else:
                list1=item+list1
        return list2

if __name__ == "__main__":
    list1=[1, [2, [3, 4], 5], 6]
    obj = FLATTEN_NESTED_LIST()
    print(obj.flatten_nested_list(list1))

"""  Find Pairs with Given Sum in a List  
● Write a function to find all pairs in a list that sum up to a given number. 
● Example  
● Input:  
List: [1, 2, 3, 4, 5, 6]  
Target Sum: 7  
● Expected Output:  
[(1, 6), (2, 5), (3, 4)]  
In this example, the pairs (1, 6), (2, 5), and (3, 4) all add up to the target sum of 7.  """

class PAIR_SUM:
    def pair_sum(self,list1,target):
        list2=[]
        for item in list1:
            for element in list1:
                if item+element == target and item not in list2 and element not in list2:
                    list2.append(item)
                    list2.append(element)
        list3=list(zip(list2[ : :2],list2[1::2])) #zip takes two list and make pair of their elements and returns zip object further convert into list.
        print(list3)
                    
if __name__ == "__main__":
    list1=[1, 2, 3, 4, 5, 6]
    target=7
    obj = PAIR_SUM()
    obj.pair_sum(list1,target)
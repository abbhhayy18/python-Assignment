"""Generate All Subsets of a Set  
● Write a function to generate all possible subsets of a given set (list) of numbers. 
Example:  
● Input:  
numbers = [1, 2, 3]  
● Expected Output:  
[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]] """
class ALL_SUBSET:
    def all_subset(self,list1):
        subsets = [[]] # [],1

        for item in list1:
            new_subsets=[]
            for j in subsets: # 
                new_subsets.append(j + [item]) 
            subsets = subsets + new_subsets 
        return subsets

if __name__ == "__main__":
    list1 = input("Enter the sets:").split()
    obj = ALL_SUBSET()
    print(obj.all_subset(list1))

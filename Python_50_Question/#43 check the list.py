""" Check if Subsequence Exists in List  
● Write a function to check if a smaller list is a subsequence of a larger list.  
Example: 
● Input:  
larger_list = [1, 3, 5, 7, 9]  
smaller_list = [3, 7]  
Expected Output:  
True  
● Input:  
larger_list = [1, 3, 5, 7, 9]  
smaller_list = [3, 8]  
Expected Output:  False """
class SUBSEQUENCE:
    def subsequence(self,list1,list2):
        if len(list1) <= len(list2):
            for i in list1:
                if i not in list2:
                    print(False)
                    break
            else:
                print(True)
        else:
            for i in list2:
                if i not in list1:
                    print(False)
                    break
            else:
                print(True)

if __name__ == "__main__":
    list1 = input("Enter list1:").split()
    list2 = input("Enter list2:").split()
    obj = SUBSEQUENCE()
    obj.subsequence(list1,list2)

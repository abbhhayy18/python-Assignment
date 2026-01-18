"""  Find the First Non-Repeated Character in a String  
● Write a function to return the first non-repeated character in a string.  
Example:  
● Input:  
string = "swiss"  
Expected Output:  
'w'  """
class NON_REPEATED:
    def non_repeated(self,str1):
        for item in str1:
            if str1.count(item) == 1:
                print(item)
                break
        else:
            print("NO non-repeated item")

if __name__ =="__main__":
    str1=input("Enter the string:")
    obj = NON_REPEATED()
    obj.non_repeated(str1)
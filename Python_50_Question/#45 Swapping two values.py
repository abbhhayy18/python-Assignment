"""Swap Two Variables Without Temporary Variable  
● Write a program to swap the values of two variables without using a temporary variable. 
Example:  
● Input:  
a = 5  
b = 10  
● Expected Output (after swapping):  
a should become 10  
b should become 5  """
class SWAPPING_VALUES:
    def swapping_values(self,val1,val2):
        val1,val2 = val2,val1
        print(f"val1 ={val1}")
        print(f"val2 ={val2}")

if __name__ == "__main__":
    val1=input("Enter first val:")
    val2=input("Enter second val:")
    obj = SWAPPING_VALUES()
    obj.swapping_values(val1,val2)
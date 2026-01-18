""" Remove Nth Occurrence of a Character from a String  
● Write a function that removes the nth occurrence of a character from a string. 
Example:  
● Input:  
string = "example example example"  
char = 'e'  
n = 2 
● Expected Output:  
"example xample example"""
class REMOVE_nth_Occurrence:
    def nth_occurrence(self,str1,char1,num):
        try:
            num=int(num)
        except:
            raise ValueError

        if num > len(str1):
            return "Occurence num is out of bound"

        str2=""
        count=-1
        for item in str1:
            if item == char1:
                count+=1
            if num == count and item == char1:
                continue
            str2=str2+item

        if count < 0:
            return f"{char1} is not found"
        else:
            return str2
            
if __name__ == "__main__":
    try:
        str1=input("Enter the string:")
        char1=input("Enter char:").lower()
        num=input("Enter the num of occurence:")
        obj = REMOVE_nth_Occurrence()
        print(obj.nth_occurrence(str1,char1,num))
    except ValueError:
        print("ERROR:Enter num in digits only->")
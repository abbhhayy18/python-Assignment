"""20. Count Occurrences of Each Character in a String  
● Take a string as input and count the occurrences of each character.  
● Example:  
Input: "hello"  
Expected Output: { 'h': 1, 'e': 1, 'l': 2, 'o': 1 }"""
class OCCURENCES:
    def __init__(self,str1):
        self.str1=str1

    def occurrences(self):
        freq={}
        for item in str1:
            freq[item]=str1.count(item)
        return freq

if __name__ =="__main__":
    try:
        str1=input("Enter the word:")
        obj = OCCURENCES(str1)
        result=obj.occurrences()
        print(result)
    except ValueError as error:
        print(error)
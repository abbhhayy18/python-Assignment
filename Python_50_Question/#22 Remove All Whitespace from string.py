"""Remove All Whitespace from a String  
● Write a function that removes all whitespace characters (spaces, tabs, newlines) from a given string.  
● Example:  
Input: "Hello, World!"  
Expected Output: "Hello,World!" """
class REMOVE_WHITESPACES:
    def remove_whitespaces(slef,str1): 
        str2=str1.replace(" ","")
        return str2

if __name__ == "__main__":
    try:
        str1=input("Enter the sentence:")
        obj = REMOVE_WHITESPACES()
        print(obj.remove_whitespaces(str1))
    except ValueError as error:
        print(error)
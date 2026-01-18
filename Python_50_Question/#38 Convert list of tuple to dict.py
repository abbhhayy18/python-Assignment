""". Convert List of Tuples to Dictionary  
● Write a function to convert a list of tuples into a dictionary. 
Example:  
● Input:  
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]  
● Expected Output:  
{'a': 1, 'b': 2, 'c': 3, 'd': 4}  """

class DICTIONARY:
    def dictionary(self,list_tup):
        if not isinstance(list_tup,list):
            raise ValueError

        dict1={}
        for item in range(len(list_tup)):
            dict1[list_tup[item][0]]=list_tup[item][1]
        print(dict1)
        

if __name__=="__main__":
    while True:
        try:
            list_tup=eval(input("Enter the list of tuples:")) # eval reads the input in str and convert it into list of tuple (eval recognize the data format given as input)
            obj = DICTIONARY()
            obj.dictionary(list_tup)
            break

        except ValueError as error:
            print(error)
        except Exception:
            print(f"ERROR:Invalid Format ! Enter list of tuple--->\nExample:[('a', 1), ('b', 2)]")
        

    
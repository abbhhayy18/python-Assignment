""" Sort Dictionary by Value  
● Write a function to sort a dictionary by its values.  
Example:  
● Input:  
{'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}  
● Expected Output (sorted by values in ascending order):  
{'banana': 2, 'date': 3, 'apple': 5, 'cherry': 8}  """

class SORT_BY_VALUE:
    def sort_by_value(self,dict1):
        if  not isinstance(dict1,dict):
            raise ValueError
        list1=sorted(list(dict1.values()))
        dict2={}
        for values in list1:
            for key in dict1.keys():
                if dict1[key] == values:
                    dict2[key] = values
                    break
        print(dict2)

            
if __name__ == "__main__":
    try:
        dict1=eval(input("Enter the dictionary :"))
        obj = SORT_BY_VALUE()
        obj.sort_by_value(dict1)
    except Exception:
        print("ERROR:Invalid Format!\n Example {'apple': 5, 'banana': 2} ")
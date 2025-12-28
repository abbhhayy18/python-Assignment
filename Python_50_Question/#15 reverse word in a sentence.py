#Example  
#Input: "Python is fun"  
#Expected Output: "fun is Python"
class REVERSE_SENTENCE:
    def __init__(self):
        pass
    def reverse_sentence(self,str1):
        str2=''
        for item in str1[::-1]:
            str2=str2+item+" "
        return str2
            
if __name__ == "__main__":
    try:
        str1=input("Enter the sentence:").split()
        obj = REVERSE_SENTENCE()
        print(obj.reverse_sentence(str1))
    except ValueError as error:
        print(error)
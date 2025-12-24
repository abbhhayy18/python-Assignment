# Anagram
# example 'silent' and 'listen' are anagram
class ANAGRAM:
    def anagram(self,st1,st2):
        
        if st1.isdigit() and st2.isdigit() or st1.isalpha() and st2.isalpha():
            for i in st1:
                if i not in st2:
                    print(f"{st1} and {st2} are not anagram ")
                    break
            else:
                print(f"{st1} and {st2} are anagram ")
        else:
            raise ValueError("ERROR:Enter the both value either string value or integer value")

if __name__ == "__main__":
    try:
        str1=input("enter the first word :")
        str2=input("enter the second word :")
        obj = ANAGRAM()
        obj.anagram(str1,str2)
    except ValueError as error:
        print(error)



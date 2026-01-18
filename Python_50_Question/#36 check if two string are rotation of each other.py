"""Check if Two Strings are Rotations of Each Other  
● Write a function to check if one string is a rotation of another.  
● Example: “abcd” and “dabc” are rotations.  
To understand why, here’s how rotation works in this context:  
If you rotate "abcd" by shifting its characters cyclically (moving some characters from 
the start to the end), you get: """

class CHECK_ROTATIONS:
    def check_rotations(self):
        str3=str1+str1
        str4=str2+str2
        if str2 in str3 and str1 in str4:
            return True
        else:
            return False

if __name__ =="__main__":
    str1=input("Enter the first string value:")
    str2=input("Enter the second string value:")
    obj = CHECK_ROTATIONS()
    print(obj.check_rotations())
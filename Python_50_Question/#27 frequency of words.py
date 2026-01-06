""" Count Frequency of Each Word in a Text File  
● Write a program to read a text file and count the frequency of each word. 
Example: File content  
Hello world  
Hello again  
Goodbye world  
Expected Output:  
Hello: 2  
world: 2 
again: 1  
Goodbye: 1 """

class FREQ_OF_WORDS:
    @staticmethod
    def freq_of_words(data):
        freq={}
        for item in data:
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1
        for key,value in freq.items():
            print(f"{key} : {value}")


if __name__ == "__main__":
    with open("freq of word.txt","r") as file:
        data = file.read().split()
    obj = FREQ_OF_WORDS()
    obj.freq_of_words(data)

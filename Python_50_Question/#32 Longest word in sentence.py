"""  Find the Longest Word in a Sentence  
● Write a function that finds and returns the longest word in a given sentence.  
Example:  
Input: "Python programming is fun and interesting"  
Expected Output: "programming"  """

class LONGEST_WORD_IN_SENTENCE:
    def __init__(self,sentence):
        self.sentence = sentence

    def longest_word_in_sentence(self):
        length=""
        for item in self.sentence:
            if len(item) > len(length):
                length = item
        return length
            
if __name__ == "__main__":
    sentence=input("Enter the sentence:").split()
    obj = LONGEST_WORD_IN_SENTENCE(sentence)
    print(obj.longest_word_in_sentence())
   
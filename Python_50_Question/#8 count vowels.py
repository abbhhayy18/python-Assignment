# count vowels
class COUNT_VOWELS:
    def count_vowel(self,words:str)->int: #word is string value and return int value
        if words.isalpha():
            vowel='aeiou'
            count=0
            for i in words:
                if i in vowel:
                    count+=1
            return count
        else:
            raise ValueError("ERROR: Enter only string value")

if __name__ == "__main__":
    try:
        words=input("Enter the words :")
        obj = COUNT_VOWELS()
        print(f"number of Vowels in {words} is :",obj.count_vowel(words))
    except ValueError as ve:
        print(ve)
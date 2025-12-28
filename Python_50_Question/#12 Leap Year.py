#Check for leap year
class LEAP_YEAR:
    def leap_year(self,year):
        try:
            year=int(year)
        except:
            raise ValueError("ERROR:Enter the year in digits only")

        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False

if __name__ == "__main__":
    try:
        year=input("Enter the year to check leap year:")
        obj = LEAP_YEAR()
        if obj.leap_year(year):
            print(f"YES {year} is a Leap Year")
        else:
            print(f"NO {year} is not a Leap Year")
    except ValueError as error:
        print(error)

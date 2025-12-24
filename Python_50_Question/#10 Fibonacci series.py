#Fibonacci series
class FIBONACCI:
    def fibonacci_seq(self,num):
        if num.isdigit():
            list1=[]
            for i in range(int(num)):
                if i < 2:
                    list1.append(i)
                else:
                    list1.append(list1[i-1]+list1[i-2])
            print(list1)
        else:
            raise ValueError("ERROR:Enter the inetger value only")
        
if __name__ =="__main__":
    try:
        num=input("Enter how many fibonacci number you want:")
        obj = FIBONACCI()
        obj.fibonacci_seq(num)
    except ValueError as ve:
        print(ve)
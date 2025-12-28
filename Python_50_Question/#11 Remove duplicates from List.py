# Remove Duplicates from list
# input:[1,3,2,3,4,1,5]
#output:[1,3,2,4,5]
class REMOVE_DUPLICATES:
    def __init__(self,list1):
        self.list1=list1

    def remove_duplicates(self):
        list2=[]
        for item in self.list1:
          if item not in list2:
            list2.append(item)
        return list2

if __name__ == "__main__":
        list1=input("Enter the list:").split()
        obj = REMOVE_DUPLICATES(list1)
        print(obj.remove_duplicates())
   
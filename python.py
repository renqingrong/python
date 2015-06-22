__author__ = 'EasyShare25'
#sum=0

#i=1
#while(i<=100):
  #  sum=sum+i
   # i+=1
#print sum

#class Employee:
 #   empCount=0
  #  def _init_(self,name,salary):
   #     self.name=name
   #     self.salary=salary
    #    Employee.empCount+=1
    #def displayCount(self):
     #   print "1"% Employee.empCount
    #def displayEmployee(self):
     #   print"Name:",self.name,",Salary:",self.salary
#emp1=Employee("rose",2000)
#emp2=Employee("jack",6000)
#emp1.displayEmployee()
#emp2.displayEmployee()
#print"1"% Employee.empCount


# sum=0
# for i in range(100):
#     i+=1
#     sum+=i;
# print sum

#import re
#line="Cats are smarter than dogs"
#matchObj=re.match(r'(.*)are(.*?).*',line,re.M|re.I)
#if matchObj:
 #   print"matchObj.group():",matchObj.group()
 #   print"matchObj.group(1):",matchObj.group(1)
  #  print"matchObj.group(2):",matchObj.group(2)
#else:
 #   print"NO MATCH!!"

#for letter in "I love you":
   #
   #  print"Current Letter:",letter

def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort(array,low,high):
     if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)
if __name__ == '__main__':
    array = [{"name":"Tom", "age":18 },
        {"name":"Alice", "age":28 },
        {"name":"Bruce", "age":8 },
        {"name":"Smith", "age":13 },
        {"name":"Cheery", "age":8 }]
    quick_sort(array,0,len(array)-1)
    print array

sum=0
i=1
for i in range(1001):
    if i%2==0:
        sum+=i
print sum






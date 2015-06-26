# -*- coding: utf-8 -*-

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
#dddd
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

# def sub_sort(array,low,high):
#     key = array[low]
#     while low < high:
#         while low < high and array[high] >= key:
#             high -= 1
#         while low < high and array[high] < key:
#             array[low] = array[high]
#             low += 1
#             array[high] = array[low]
#     array[low] = key
#     return low
#
#
# def quick_sort(array,low,high):
#      if low < high:
#         key_index = sub_sort(array,low,high)
#         quick_sort(array,low,key_index)
#         quick_sort(array,key_index+1,high)
# if __name__ == '__main__':
#     array = [{"name":"Tom", "age":18 },
#         {"name":"Alice", "age":28 },
#         {"name":"Bruce", "age":8 },
#         {"name":"Smith", "age":13 },
#         {"name":"Cheery", "age":8 }]
#     quick_sort(array,0,len(array)-1)
#     print array
#aa
# sum=0
# i=1
# for i in range(1001):
#     if i%2==0:
#         sum+=i
# print sum
# import requests
# from os.path import dirname,abspath
# from extract import extract,extract_all
# import re
# RE_CN=re.compile(ur'[\u4e00-\u9fa5]+')
# PREFIX=dirname(abspath( _ file _ ))
# with open("%s/down.bat"%PREFIX,"w")as down:
#     for i in xrange(1,306):
#         for url in("http://www.luoo.net/radio/radio%s/mp3.xml"%i,
#                    'http://www.luoo.net/radio/radio%s/mp3player.xml'%i ):
#             r=requests.get(url)
#             print url
#             if r.status_code==200:
#                 for path,name in zip(
#                      extract_all('path="', '"', r.content),
#                     extract_all('title="', '"', r.content)
#                 ):
#                     if RE_CN.match(name.decode('utf-8', 'ignore')):
#                         down.write('wget %s -O "%s/%s.mp3"\n'%(
#                            path,PREFIX,name.decode('utf-8',
#                             "ignore").encode("gb18030","ignore")))
#                 break

# import math
# for i in range(1,1000):
#     x=int(math.sqrt(i+100))
#     y=int(math.sqrt(i+168))
#     if x*x==(i+100)and y*y==(i+168):
#         print i


# sum=0
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a<>b and a<>c and b<>c:
#                 print a*100+b*10+c
#                 sum+=1
# print sum

# result=[8,19,6]
# for i in range(0,3):
#     #input=int(raw_input("please enter an integer:/n"))
#     result.append(input)
# result.sort()
# print result
# a=[1,2,3,4]
# a.reverse()
# print a

# for i in range(1,10):#1-10
#     for j in range(1,10):
#         if j<=i:
#             #print'{0}*{1}={2}'.format(i,j,i*j),
#             print "%s*%s=%s"%(str(i),str(j),str(i*j))
#             print
# import sys
# for i in range(1,9):
#     if i==1:
#         sys.stdout.write('@@')
#         sys.stdout.write('\n')
#     else:
#          for j in range(1,9):
#              if j<=i:
#                 sys.stdout.write("*"),
#          print
# result=[]
# for x in range(1,10):
#     for y in range(0,10):
#         for z in range(0,10):
#             m=100*x+10*y+z
#             if m==x**3+y**3+z**3:
#                 result.append(m)
# print result
# print "Hello World!"
# print "Hello Again!"
# print "I like typing this."
# print "This is fun."
# print "Yay!Printing."
# print "I'd much rather you 'not'."
# print 'I "said" do not touch this.'
# print"I like you very much !"
# print'"xiao de se" is interesting'
# print "What is wrong with you and 'How are you'"
# print"I like eat"
# sum=0
# for i in range(1,101):
#     sum=sum+i
#     i=i+1
# print sum

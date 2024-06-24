


# LOOPS :- It is used to repeat the set of number.
# it is used to set iteratition


# LOOPS TYPES:- 

# While loop :- 

# For loop :-  


#-------------------------------1 April,2024-------------------------------------------------

# WHILE LOOP

# x=10
# y=1

# while x>y:
# 	print(x)
# 	x=x-1


# print the counting from 1 to 50

# x=1
# while x<51:
# 	print(x)
# 	x+=1

# print counting from 20 to 1

# x=20
# while x>0:
# 	print(x)
# 	x-=1


# print the number from 10 to 40 but step size should be 2


# x=10
# while x<41:
# 	print(x)
# 	x+=2


# Print the even number from 1 to 20 

# x=1
# while x<11:
# 	print(x*2)
# 	x+=1

#                  OR

# x=1
# y=20

# while x<=y:
# 	if x%2==0:
# 		print("Even number : ",x)
# 	x+=1



#Print all the odd number from 1 to 20 

# x=1
# y=20

# while x<=y:
# 	if x%2!=0:
# 		print("Odd number ",x)
# 	x+=1


# x=int(input("Enter any number:- "))
# y=1

# while x>=y:
# 	if y%2==0:
# 		print("Even numbers :- ",y)
# 	y+=1


# print the table of 5


# x=5
# while x<51:
# 	print(x)
# 	x+=5
#                   OR

# x=1 
# while x<11:
# 	print(x*5)
# 	x+=1



# Print any table by user input 

# x=1
# y=int(input("Enter any number:- "))

# while x<11: 
# 	print(x*y)
# 	x+=1

# Print like thiss:

# 5 X 1 =5
# 5 X 2 =10
# 5 X 3 =15
# 5 X 4 =20
# 5 X 5 =25
# 5 X 6 =30

# x=1
# y=int(input("Enter any number:- "))

# while x<11: 
# 	print(y,"X",x,"=",x*y)
# 	x+=1

#                 OR


# x=1
# y=int(input("Enter any number:- "))

# while x<11: 
# 	print(f"{y} X {x} = {x*y}")
# 	x+=1


#Count total number of even from 1 to 20

# x=0
# y=2
# while y<=20:
#     x+=1
#     print(y)
#     y+=2
# print("Total even numbers:",x)

#          OR

# y=int(input("Enter the number :- "))
# x=1
# c=0
# while x<=y:
#     x+=1
#     if x%2==0:
#         c+=1
# print("Total number of even number:- ",c)

# Count total number of odd from 1 to 30-------------------------------------

# x=0
# y=1
# while y<=30:
#     x+=1
#     print(x)
#     y+=2
# print("Total odd numbers:",x)


# x=int(input("Enter the number :- "))*2
# y=1
# while x>y:
#     if y%2==0:
#         print("Total number of even number:- ",y)
#     y+=1


# x=int(input("Enter odd numbers:- "))
# y=0
# z=0
# while x>y:
#     z=z+1
#     if z%2!=0:
#         print("Odd number :- ",z)
#         y=y+1



''' BREAK STATEMENT '''

# x=10
# y=1
# while x>=y:
#     print(y)
#     if y==5:
#         break
#     y+=1


# OR


# y=1
# while y<=20:
#     if y==10:
#         break
#     else:
#         print(y)
#     y+=1


''' CONTINUE STATEMENT '''



# x=10
# y=0

# while x>y:
#     y+=1
#     if y==5:
#         continue
#     else:
#         print(y)






#print the number from 1 to 15 and skip the number 7 and 10

# x=15
# y=0

# while x>y:
#     y+=1
#     if y==7 or y==10:
#         continue
#     else:
#         print(y)


#print the number from 1 to 10 and break the loop where number is 6


# x=10
# y=0
# while x>y:
#     y+=1
#     if y==6:
#         break
#     else:
#         print(y)

# print the number from 20 to 30 and skip the number 26,28,30

# x=30
# y=20

# while x>y:
#     y+=1
#     if y==26 or y==28 or y==30:
#         continue
#     else:
#         print(y)


# print the back count from 50 to 10 and break the loop where number is 20


# x=10
# y=50
# while y>=x:
#     if y==20:
#         break
#     else:
#         print(y)
#     y-=1

# find sum of first 5 numbers

# x=1
# y=5
# s=0
# while y>=x:
#     s=s+x
#     x+=1
# print("total sum:- ",s)


# find avg of first 10 numbers


# x=0
# y=10
# a=0
# while y>x:
#     x+=1
#     a=a+x/y
# print(a)



# x=int(input("Enter number :- "))
# y=1
# m=1
# while x>=y:
#     m=m*y
#     y+=1
# print("Factorial of number:- ",m)

# print delhi in individual statement

# x="Delhi"
# y=len(x)
# z=0
# while y>z:
#     print(x[z])
#     z+=1


#--------------------------4 April,2024---------------------------------------

# print(x)  # it prints vertically


# print(x,end="")   # it prints horizontally


# x="Delhi"
# y=len(x)
# z=0
# while y>z:
#     print(x[z],end="--")
#     z+=1


# x=1 
# while x<=15:
#     print(x,end="--")
#     x+=1


# print hello world 20 times 


# x=0
# y=20
# z="hello world"
# while y>=x:
#     print(z)
#     x+=1


#x="dAta SCIence"

# extract all the capital letter of alphabet

# y=len(x)
# z=0
# while y>z:
#     if x[z].isupper():
#         print(x[z])
#     z+=1


###############----- FOR LOOPS -----####################


# Sequence data :- list[], tuple{}, range()

#1 - 20 

# for x in range(1,21):
#     print(x)


# print number from 1 to 100 

#for x in range(1,101):
#   print(x)

# print number from 200 to 250 horizontally 

# for x in range(200,251):
#    print(x,end=" ")

# print all even number between 20 to 50

# for x in range(20,51):
#     if x%2==0:
#         print(x)

# print back counting from 50 to 1

# for x in range(50,0,-1):
#     print(x)



# print the counting with the help of user input 

# x = int(input("Enter the number :- "))+1
# for i in range(1,x):
#     print(i)


#--------------------------------8 April,2024-------------------------------------


# range(10)
# range(1,15)
# range(10,30,3)

# for i in range(100,0,-1):
#     print(i,end=" ")


# even number from 10 to 30
# for i in range(10,31):
#     if i%2==0:
#         print(i)

# for i in range(10,31,2):
#     print(i)



# print and count the leap year from 1947 till now 

# c=0
# for i in range(1947,2025):
#     if i%4==0:
#         print("Leap year:- ",i)
#         c+=1
# print("Total number of leap years:- ",c)


#   print table using user input 

# i=int(input("Enter any number:- "))
# for x in range(1,11):
#     print(i," X ",x," = ",i*x)
    



#   print factorial using user input

# f=1
# x=int(input("Enter number:- "))
# for i in range(1,x+1):
#     f=f*i
# print("Factorial of number is:- ",f)



# print the reverse counting from 50 to 10

# for i in range(50,9,-1):
#     print(i)

# print the reverse counting from 100 to 50 
# and step size should be 5

# for i in range(100,49,-5):
#     print(i)


#x= "Himachal Pradesh"

#while loop

# y=len(x)
# z=0
# while y>z:
#     print(x[z])
#     z+=1

# for loop

#for i in x:
#    print(i)


#import time

# for i in range(10):
#     print(i)
#     time.sleep(2)


# for i in range(30,0,-1):
#     print(i,end="\r")
#     time.sleep(1)


# Escape function:-

# print("Hello\tworld")   # gives tab space between string

# print("Hello\nworld")   # print string in next line

# print("Hello\rworld")   # replace string with previous one


# print the each alphabet of "hello world" 
# with the help of for loop
# x="Hello World"
# for i in x:
#     print(i)

#print 10 times your name with the help of for loop

# x="Vishwas"
# for i in range(0,10):
#     print(x)



#  windows +  .     (Brings emoji)


#BREAK

# for i in range(1,1000):
#     if i==50:
#         break
#     else:
#         print(i)

#CONTINUE

# for i in range(1,15):
#     if i==5 or i==10:
#         continue
#     else:
#         print(i)


# write a python program to print the number from 4 to 50 and exclude 
# all the number divisible by 5 and 10


# for i in range(4,51):
#     if i%5==0 or i%10==0:
#         continue
#     else:
#         print(i)



#----------------------10 April,2024---------------------------#



# count the total number of even number from 1 to 20

# c=0
# for i in range(1,21):
#     if i%2==0:
#         print(i)
#         c+=1
# print("Total even numbers",c)

# find the sum of first 10 number

# s=0
# for i in range(1,11):
#     print(i)
#     s=s+i
# print("Total sum",s)

# find the sum of first 10 even number

# s=0
# for i in range(1,21):
#     if i%2==0:
#         print(i)
#         s=s+i
# print("Total sum",s)


# count total number from 10 to 30 whose divisible of 2 and 3

# c=0
# for i in range(10,31):
#     if i%2==0 and i%3==0:
#         print(i)
#         c+=1
# print("Total count",c)



# x="india1223@#$"
# # output= i*n*d*i*a

# for i in x:
#     if i.isdigit():
#         break
#     else:
#         print(i,end="*")




# x="Hello world"

# print(x.count("o"))

# print(x.index("o"))



# x="Himachal pradesh"
# for i in x:
#     if i=="a":
#         print(i)


# find the index of x and print it in individual line

# c=0
# x="Himachal pradesh"    
# for i in x:
#     print(i,c)
#     c+=1

#     OR


# x="Himachal Pradesh"

# y=len(x)

# for i in range(y):
#     print(x[i],"+ve:",i,"-ve:",i-y)


# find index of a

# c=0
# x="Himachal pradesh"    
# for i in x:
#     if i=="a":
#         print(i,":",c)
#     c+=1

#      OR


# x="Himachal pradesh"
# y=len(x)
# for i in range(y):
#     if x[i]=="a":
#         print(x[i]," : ",i)


# x="data123science@#$4"


# count total alphabet

# c=0
# for i in x:
#     if i.isalpha():
#         print(i)
#         c+=1
# print(c)

# count total number of digit

# c=0
# for i in x:
#     if i.isdigit():
#         c+=1
# print(c)

# count total number of special charactor

# c=0
# for i in x:
#     if not i.isalnum():
#         c+=1
# print(c)

###########OR##############

# x = "data123s324453@#$cience@#$4"

# n = 0
# c = 0
# s = 0

# for i in x:
#     if i.isdigit():
#         n = n + 1
#     elif i.isalpha():
#         c = c + 1
#     else:
#         s = s + 1


# print("Total Number of text :- ",c)

# print("Total Number of digit :- ",n)
# print("Total Number of special charactor :- ",s)




#---------------------------11 April,2024----------------------------




########################### Nested loop  ##########################


# for i in range(1,5):
#     print("---------")
#     for j in range(6):
#         print(j)


# for i in range(10):
#     for j in range(i):
#         print(j,end=" ")
#     print( ) 


# for i in range(10):
#     for j in range(10-i):
#         print(j,end=" ")
#     print()


# for i in range(10):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# x=["apple","mango","guava"]

# for i in x:
#     for j in i:
#         print(j)


# show the square of each value from 1 to 20

# for i in range(1,21):
#     print(i,"=", i*i)

# show the cube of number from 1 to 20

# for i in range(1,21):
#     print(i,"=",i*i*i)

# write a python program to display all 
# prime number from 25 to 50

# for i in range(25,51):
#     if i%i==0 and i%2==0:
#         break
#     else:
#         print(i)


# reverse the given integer 
# input = 7894
# output = 4987
# x="7894"
# print(x[::-1])


# Write a Python program to get a string from a given string where all occurrences
# of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'



# Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
# Click me to see the sample solution



# Write a Python program to remove characters that have odd index values in a given string.
# X = "Databases"


# Write a Python program to check whether a string starts with specified characters.

################################# 25 April,2024 ################################################

#1.
# Write python program to show Discounted Amount
# if amount is between 4k to 6k then 40%
# if amount is between 2k to 4k then 30%
# if amount is betweeen 1k to 2k then 20%
# else 10%

# x=int(input("enter any number:- "))

# if 1000<=x<2000:
#     d=x*0.4
#     a=x-d
# elif 2000<=x<4000:
#     d=x*0.3
#     a=x-d
# elif 4000<=x<=6000:
#     d=x*0.2
#     a=x-d
# else:
#     d=x*0.1
#     a=x-d
# print("MRP : ",x)
# print("Discount : ",d)
# print("After Discount : ",a)

# 2.
# write a python to show the grade of the student 
# if student marks is >=90 then show A+
# if student marks is >=85 then show A
# if student marks is >=80 then show B+
# if student maarks is >=70 then show B
# if student marks is >=60 then show C
# if student marks is >=50 then show D
# else show E

# x=int(input("enter percentage:- "))

# if x>=90:
#     print("A+")
# elif x>=85:
#     print("A")
# elif x>=80:
#     print("B+")
# elif x>=70:
#     print("B")
# elif x>=60:
#     print("C")
# elif x>=50:
#     print("D")
# else:
#     print("E")


# 3.
# write a python program to exchange the values
# in other variables

# x = 10
# y = 20
# z = 30
# output :-
# x = 30
# y = 10
# z = 20

# x = 10
# y = 20
# z = 30
# print("Before")
# print("x=",x)
# print("y=",y)
# print("z=",z)

# x,y,z=z,x,y

# print("After")
# print("x=",x)
# print("y=",y)
# print("z=",z)


# x= "Ansh Raj"

# y=len(x)

# for i in range(y):
#     print(x[i],i,i-y)


# x="gfubjokfgbrgnj19404fvkjdfvkjdenf23fh9284r"

# for i in x:
#     if i.isalpha():
#         print(i,end="")
# print(type(i))


# x="gfubjokfgbrgnj19404fvkjdfvkjdenf23fh9284r"
# y=""
# for i in x:
#     if i.isalpha():
#         y+=i
# print(y)
# print(type(y))


# Write a python program to count all the number who 
# is divisible by 5 and 7 btw 1 to 100

# c=0
# for i in range(1,101):
#     if i%5==0 and i%7==0:
#         c+=1
#         print(i)
# print("total no. divisible by 5 and 7:- ",c)

#write a python program from printing reverse counting from 50 to 1

# x=50
# for i in range(1,51):
#     print(x)
#     x-=1

# x="Data Science"
#reverse the string
# output:- ecneics atad

# y=len(x)
# for i in range(y):
#     y-=1
#     print(x[y],end="")


####################### 26, april,2024 #######################################


# x=int(input("enter the number :- "))
# if x>1:
#     for i in range(2,(x//2)+1):
#         if x%i==0:
#             print(x,"Not prime")
#             break
#     else:
#         print(x,": is prime")
# else:
#     print(x,"is not a prime")


# x="Data science"

# x=x.split()
# x=x[-1::-1]
# x=" ".join(x)
# print(x)


 
# x=["a","b","c","d"]
# y=["g","c","d","a","r","o"]

# for i in x:
#     for j in y:
#         if i==j:
#             print(j)


# for i in y:
#     if i in x:
#         print(i)


# count total prime no. from 1 to 50 




#-----------------------LIST-------------------------------------------


# LIST:- list is used to store multiple values in single variable 

# 1. list are written in square bracket[]
# 2. list is changable or mutable
# 3. list allow duplicate values
# 4. here we can enter multiple type of data
# 5. list is indexed
# 6. list or ordered


# x=["prince",24,5.4,true,false]


# x=["ansh","vishwas","simran","yogesh","ansh"]

# print(x)
# print(type(x))  
# print(len(x))

# indexing :- it is used to extract the single text from the text

# type of indexing :- 1. positive 2. negative

# slicing:- it is used to extract the range of text from the list

#################################################################

# x=["ansh","simran","vishwas","manjeet","yogesh","anshu","harmeet"]

# extract 

# ansh
# print(x[0],x[-7])
# manjeet
# print(x[3],x[-4])
# manjeet yogesh, anshu
# print(x[3:6])


#Slicing:- 

#x=[1,2,3,4,5,6,7,8,9,10]

#print(x[1:10:2])


# DELETE 

# 1. remove 
# 2. pop
# 3. clear
# 4. del

#create a list and insert all the values of month 

# x=["jan","feb","mar","apr","may","jun","jul","aug","sept","oct","nov","dec"] 

#1. remove 

# print(x)
# print(x.remove("jan"))

# print("after",x)


#2. pop

# print(x)
# print("---------------------------------------------")

# x.pop()
# print(x)
# x.pop(2)
# print(x)


#3. clear

# print(x)
# print("------------------------------")
# x.clear()
# print(x)

#4. del

# del x[0]
# print(x)



#####  FOR PRIME NO.  ################

# x = 50
# c = 0

# for a in range(2,x+1):
#     if a>1:
#         for i in range(2,(a//2)+1):
#             if a%i==0:
#                 break
#         else:
#             print(a,"is a prime number")
#             c+=1
# print("Total no. of prime number :- ",c)

###################### 29 April,24 #########################


# x=["sun","mon","tue","wed","thu","fri","sat"]

#1. delete 3rd index of value 

# del x[3]
# print(x)

#2.extract ["fri","sat"]
# print(x[5:])

#3.extract "sun"
# print(x[0])

#4. delete "mon"

# x.remove("mon")
# print(x)

#5. Delete all values from the list

# x.clear()
# print(x)

#6. Delete last value from the list

# x.pop()
# print(x)


########### ADDING VALUES IN LIST ################

# 1. Insert :- with the help of insert we can add 
#              values acc. to index.

# x=["sun","mon","tue"]

# print(x)
# x.insert(1,"data")
# x.insert(0,"sci")
# print(x)

# 2. Append :- it is used to add the values from end 
#              of the list.

# x=["sun","mon","tue"]

# x.append("wed")
# print(x)

# 3. Extend :- it is used to add multiple values in list.

# x=["sun","mon","tue"]

# x.extend(["wed","thu","fri"])
# print(x)

# x=["sun","mon","tue"]
# y=["wed","thu","fri"]

# x.extend(y)
# print(x)
# print(x+y)

# x=str(x)
# print(x.upper())
# x=list(x)
# print(x)

# x=[4,7,8,2,1,4,5,6,8,3]

#sort:- it is used to arrange the data in asc or desc order


#Ascending order
# x.sort()
# print(x)

#descending order
# x.sort(reverse=True)
# print(x)


# x=[12,45,78,89,56,10,60,]


# 1. maximum value from list 

# x.sort()
# print(x[-1])

# 2. minimum value from list 

# x.sort()
# print(x[0])

# 3. 3rd maximum value from list

# x.sort(reverse=True)
# print(x[2])

# 4. 2nd minimum value from list

# x.sort()
# print(x[1])


# print(min(x))
# print(max(x))

# print(x.index(89))
# print(x[4])


# x=["sun","mon","tue"]

# y=x.copy() #copy() is used to copy the value of variable 
# #                # without changing value
# x.clear()
# # print(y)
# # print(x)

# for i in y:
#     i=i.upper()
#     x.append(i)

# print(x)
# print(type(x))

# x=[45,78,89,12,45,56,23,10]

# print all the number who is less than 30

# for i in x:
#     if i<30:
#         print(i)


# print all the numbers who is greater than 40

# for i in x:
#     if i>40:
#         print(i)



# x=[45,78,89,12,45,56,23,10]

#1. delete all the value that is less than 30

# for i in x[:]:
#     if i<30:
#         x.remove(i)
# print(x) 

#OR

# y=x.copy()
# x.clear()
# for i in y:
#     if i <30:
#         continue
#     else:
#         x.append(i)
# print(x)

# x = [12,45,56,3,12,3,12,8,12]

# 2. create a new blank list and add all the even
#   values in list

# y=list()

# for i in x:
#     if i%2==0:
#         y.append(i)
#     else:
#         continue
# print(y)


#3. print all duplicate values 

# for i in x:
#     if x.count(i)>1:
#         print(i,end=" ")
   

#4. print all unique number

# y=[]
# for i in x:
#     if i not in y:
#         y.append(i)

# print(y)

#5. print negative and positive index of all number in list

# y=len(x)

# for i in range(x):
#     print(x[i],i,i-y)


#---------------------30 April, 2024----------------------------


#Print values of list x in y except string

# x=["jan",45,"aug",42.9,"sun",True,21j]
# y=[]

# for i in x:
#     if type(i)==str:
#         continue
#     else:
#         y.append(i)
# print(y)


####################### Nested list #########################


# x=[21,43,[45,67,8,100],200]
# print(x)
# print(type(x))
# print(len(x))


# x=[12,[45,78,89,100,200,456],789]

#Extract values 

# 12
# print(x[0])
# 45
# y=x[1]
# print(y[0])
#OR
# print(x[1][0])
# 200
# print(y[4])
#OR
# print(x[1][4])
# 789
# print(x[2])
# 89
#OR
# print(x[1][2])
# print(y[2])


# x=[100,200,[300,400,[500,600,700],800,900],1000]

# # 800
# print(x[2][3])
# # 600
# print(x[2][2][1])
# # 300
# print(x[2][0])
# # 200
# print(x[1])
# # 1000
# print(x[3])


# x = [[12,78,[[14,10,11],23,56,[89,96,25]],63,[23,100],123]]

# # print(x)

# # Extract all Number from the List
# # 1.  10
# print(x[0][2][0][1])
# # 2.  11
# print(x[0][2][0][2])
# # 3.  12
# print(x[0][0])
# # 4.  56
# print(x[0][2][2])
# # 5.  100
# print(x[0][4][1])
# # 6.  63
# print(x[0][3])
# # 7.  14
# print(x[0][2][0][0])
# # 8.  89
# print(x[0][2][3][0])
# # 9.  96
# print(x[0][2][3][1])
# # 10. 78
# print(x[0][1])
# # 11. 123
# print(x[0][5])

#--------------------------------1 May,2024----------------------------------

# x=[12,45,56,89,12,56,12,10,12]
# y=len(x)
# 1. find the index of all 12

# for i in range(y):
#     if x[i]==12:
#         print(x[i],"index:- ",i)

# 2. find the sum of number with the help of loop
# y=0
# for i in x:
#     y+=i
# print(y)

# x=[1,2,4,1.2,5.9,10.8,"a","b","c",True,21j]

#3. count total number of text from the list 
# c=0
# for i in x:
#     if type(i)==str:
#         c+=1
# print(c)


#4. count all numerical data from the list


# c=0
# for i in x:
#     if type(i)==int or type(i)==float or type(i)==complex:
#         c+=1
# print(c)



################  TUPLES  ####################


# TUPLES() :- TUPLE ARE USED TO STORE THE MULTIPLE VALUES IN A SINGLE 
# VARIABLE


# 1. TUPLES ARE WRITTEN IN ROUND BRACKET
# 2. TUPLES ARE UNCHANGABLE
# 3. TUPLES ALLOW DUPLICATE VALUES
# 4. TUPLES ARE ORDERED
# 5. TUPLES ARE INDEXED
# 6. TUPLES ALLOW MULTIPLE TYPE OF DATA




# Blank tuple

# x=()
# print(x)

# y=tuple()
# print(y)

# Blank list

# x=[]
# y=list()

# print(x)
# print(y)


# x=("a","b","c","d","e",1,2,3,4,True,21j)

# print(type(x))

# print(len(x))

# Type CASTING:- CHANGING DATATYPE OF ANY VARIABLE
# SWAPPING :- CHANGING THE VALUES OF ANY VARIABLE

# x=list(x)
# print(x)


# x=120
# y=str(x)

# a,b=y,"10"
# print(a+b)


# Packing and Unpacking

# Packing a tuple
# when we create a tuple, we normally assign values to it.
# This is called packing a tuple.

# Unpacking a Tuple
# When we create a tuple, we normally assign values to multiple variable
# from a tuple, this is called unpacking.


# x = ("First","Second","Third")
# a,b,c = x
# print(a)
# print(c)
# print(b)


# x=(45,78,89,56)

# a,*b,c=x

# print(c)

# x=("sunday","monday","tuesday","wednesday","thursday")

# a,*b,c=x

#--------------------------2 May,2024--------------------------------------------


# x=(12,45,78,89,5,23,10,18,45)

# # 1. Store all even number from new list 

# # y=[]
# # for i in x:
# #     if i%2==0:
# #         y.append(i)
# # print(y)

# # 2. store all odd numbers from new list
# # y=[]

# # for i in x:
# #     if i%2!=0:
# #         y.append(i)
# # print(y)
# ##############################################

# x=(23,34,4,45,5,6,56,6,7,6,3,3,23)


# # count

# i=x.count(3)
# print("Total count of 3 in x:- ",i)

# # index

# i=x.index(45)
# print("Index of 45:- ",i)

# # sum

# i=sum(x)
# print("Sum of x:- ",i)

# # min

# i=min("minimum value:- ",x)
# print(i)

# # max

# i=max("maximum value:- ",x)
# print(i)

# # sorted

# i=tuple(sorted(x))
# print("Sorted:- ",i)

###### SORT AND SORTED ######################

# SORT:- IT IS USED IN LIST ONLY. HERE I AM NOT 
# TAKING ANY VARIABLE.


# SORTED:- IT IS USED IN LIST, TUPLE, SET DICT,
# HERE WE ARE NOT USING ANY VARIABLE.



# x= ["ram","sita","krishan"]

# replace ram by ramayan 

# x[0]="ramayan"
# print(x)

# x.pop(0)
# x.insert(0,"ramayan")
# print(x)




# x= ("ram","sita","hanuman")

# #sita=krishna

# x=list(x)
# x[1]="Krishna"

# print(tuple(x))



# x=(78,89,45,56,78,52,62,10)


# 1. find the 2nd index of 78

# i=x.index(78,2)
# print(i)

# 2. find the sum of last 3 Number.

# i=sum(x[5:])
# print(i)

# 3. reverse the Tuple

# x=list(x)
# x.reverse()
# print(x)

# 4. Create a list with the help of user input

# x=[]
# y=int(input("Enter length of list:- "))

# for i in range(y):
#     i=input("Enter values:- ")
#     x.append(i)
# print(list(x))

#5. Create a tuple with the help of user input 

# x=[]
# y=int(input("Enter length of list:- "))

# for i in range(y):
#     i=input("Enter values:- ")
#     x.append(i)
# print(tuple(x))

#################################################################


# 1. Write a program with the help of user input to display the last digit of a number

# x=str(input("Enter any number:- "))
# print(x[-1])
###OR###
# x=int(input("Enter the number:- "))
# print("Last digit is: ",x%10)

# 2. write a program to caluculate the electricity bill
# if number of unit is less than 200 then 5 rupees per unit 
# else 10 rupees per unit

# x=int(input("Enter the unit:- "))
# if x<200:
#     print("Your bill is ",x*5,"rs")
# else:
#     print("Your bill is ",x*10,"rs")

# 3. Write a program with the help of user input to check the Number is 
#         divisible of 5,7 and 9 or Not ?

# x=int(input("Enter any number:- "))
# if x%5==0 and x%7==0 and x%9==0:
#     print(x," is divisible")
# else:
#     print(x,"Not divisible")


# 4. print the statement 
#     HOnesty is the best Policy ---- if strings  is vowel
#     else print Consonent

# x=str(input("Enter any alphabet:- "))

# if x in ("a","e","i","o","u"):
#     print("Honesty is best policy")
# else:
#     print("consonent")

# 5. write a program with the help of two user input if the sum 
#of two Number is even then print even Number with the value of sum
# else print number is odd with values.

# x=int(input("Enter any number:- "))
# y=int(input("Enter any number:- "))

# if (x+y)%2==0:
#     print(x+y,"is even number")
# else:
#     print(x+y,"is odd number")


# 6. If Number is between the 100 to 200 and 400 to 600 then Print
#     Done else print Not Done

# x=int(input("Enter any number:- "))
# if 100<x<200 or 400<x<600:
#     print("Done")
# else:
#     print("Not done")


# 7. write a program with the help of user input and print the Number
#     if Number is divisible of 2,4 and 6 else print Number is not
#     divisible of 2,4 and 6




# 8. Write a python program to show if length of text is greater than 5
# then show the last 2 alphabet
#     else show beginning of 2 alphabet.
 
# 9. Write a python program to print the number from 1 to 50 the Number
# who is divisible of 5 and 4

#10.  write a python program with the help of user input to compare in  three 
#  number and show gretest number.




#------------------------------20 May,2024------------------------------------

# data type :
#       1. numerical :- int float complex
#       2. text :- str
#       3.sequence :- list tuple range
#       4.boolen :-True, False
#       5.set :- set
#       6.mapping :- dictionary  dict
#       7.None
#       8.Binary


# int :-  whole number 
# float :- Decimal Number
# complex :- 21j



# list : List are used to store the multiple values in a single variable
# 1. List are written in square Bracket
# 2. it is changable or Mutable
# 3. it allow duplicate values
# 4. it is ordered
# 5. Here we store multiples type of data.
# 6. it is indexed


# Tuple :-
# 1. ()
# 2. UNCHANGABLE or immutable
# 3. allow duplicate values
# 4. ordered
# 5. indexed
# 6. multiple data type allow

# string :- strings are written in dual quatation or single quatation


# loop :-


#  break / continue

#  type casting :-

# x = [ 12,45,78,9,65]


# #delete
# 1. remove :- x.remove(12)
# 2. pop :- x.pop(2)  # 78
# 3. del :- del x[0]
# 4. clear :- delete all the values

# # add
# 1.append :- it is used to add the value in a list last of index 
# 2.insert :-
# 3.extend :-


# # string

# x  = "python"

# x.index("o")
# x.find("o")

# x = "python"
# x.reverse()
# x[-1::-1]




# x,y,z =1,2,56

# x,y = y,x
# z,x = x,z

# # x = ?  56   56  56  56
# # y = ?  1    1   2   1
# # z = ?  1    2   1   56

# print("x",x)


# print("y",y)

# print("z",z)


#   operators

# 1. Airthmatic
# 2. Membershiop
# 3. Comperision
# 4. Assignment
# 5. Logical
# 6.Bitwise
# 7. identity



# # logiccal operators :-
#   and
#   or 
#   not

# # identity :-  
# is 
# is not

# # memebership
# in 
# not in

# # 


#tuple:

# packing :- 
# unpacking :-



# print the total even number between 1 to 15
# for i in range(1,16):
#   if i%2==0:
#       print(i,end = "  ")


# count all odd number between 1 to 20
# c = 0
# for i in range(1,21):
#   if i%2!=0:
#       c+=1
# print("Total Numebr of Odd Number :- ",c)

# find the average of first 5 number

# c = 0
# s = 0
# for i in range(1,6):
#   s += i
#   c += 1

# avg = s/c
# print("Average :- ",avg )


#-----------------------------21 May,2024------------------------------------------


#print the number from 1 to 10 with the help of while loop and skip 4,6,8

# x=0
# y=10
# while x<y:
#     x+=1
#     if x==4 or x==6 or x==8:
#         continue
#     else:
#         print(x)


# print table with the help of user input

# x=int(input("Enter any number= "))
# for i in range(1,11):
#     print(i*x)
  

# x="data310science23"

# print all the integer from the string
# for i in x:
#     if i.isdigit():
#         print(i,end=" ")

# print all the text from the string
# for i in x:
#     if i.isalpha():
#         print(i,end=" ")


# x="df34@##sd$%"

# for i in x:
#     if i.isalpha() or i.isdigit():
#         continue
#     else:
#         print(i)

# x=[34,5,56,7,71,12,45,78,]

#1. replace second value 5 at the place of 100

# x[1]=100
# print(x)


#2 print all even number from list 

# for i in x:
#     if i%2==0:
#         z.append(i)
# print(z)

#3 delete 3rd index of value

# x.pop(3)
# print(x)

#4 count all odd number.
 
# c=0 
# for i in x:
#     if i%2==1:
#         c+=1

# print("Total odd number :- ",c)



# x=(12,45,7,89,5,65)

#1. sort in ascending order 

# x=sorted(x)
# print(tuple(x))

#2. sort in decending order 

# y= sorted(x,reverse=True)
# print(tuple(x))


#3. reverse the tuple

# y=reversed(x)
# print(tuple(y))

#4. show the index of 7

# print(x.index(7))


# x="data science"

# find the second index of a 
# print(x.find("a",2))

#sci
# print(x[5:8])

#ta
# print(x[2:4])

#last 3 alphabet
# print(x[-3:])



# x=(12,45,78,45,56,89,45,12)
# extract all duplicate values

# for i in x:
#     if x.count(i)>1:
#         print(i)


#show all unique values
# change the datatype in string in tuple of all values
#------------------------------------------------------------------------------------------------------------------
# SETS{}


# add()   Adds an element to the set
# clear() Removes all the elements from the set
# copy()  Returns a copy of the set
# difference()    Returns a set containing the difference between two or more sets
# difference_update() Removes the items in this set that are also included in another, specified set
# discard()   Remove the specified item
# intersection()  Returns a set, that is the intersection of two other sets
# intersection_update()   Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()    Returns whether two sets have a intersection or not
# issubset()  Returns whether another set contains this set or not
# issuperset()    Returns whether this set contains another set or not
# pop()   Removes an element from the set
# remove()    Removes the specified element
# symmetric_difference()  Returns a set with the symmetric differences of two sets
# symmetric_difference_update()   inserts the symmetric differences from this set and another
# union() Return a set containing the union of sets
# update()    Update the set with the union of this set and others


#----------------------------------23 May,2024--------------------------------------------------------------------------


# LIST():-

# 1. []
# 2. ALLOW DUPLICATE VALUES
# 3. ORDERED
# 4. CHANGABLE OR MUTABLE
# 5. INDEXED
# 6. MULTIPLE DATA TYPE

# TUPLE():-

# 1. ()
# 2. ALLOW DUPLICATE VALUES
# 3. ORDERED
# 4. UNCHANGABLE 
# 5. INDEXED
# 6. MULTIPLE DATA TYPE


# SET():- 

# 1. {}
# 2. DONT ALLOW DUPLICATE VALUES
# 3. UNORDERED
# 4. CHANGABLE OR MUTABLE
# 5. UNINDEXED
# 6. MULTIPLE DATA TYPE


# DICTIONARY():- IT IS A COLLECTION OF NON REPETATIVE ELEMENTS.
# IT IS ALWAYS SEEN IN KEY AND VALUE PAIRS.

# 1. {KEY:VALUES}
# 2. ORDERED
# 3. CHANGABLE OR MUTABLE
# 4. UNINDEXED
# 5. MULTIPLE DATA TYPE
# 6. DONT ALLOW DUPLICATE VALUES 





# how to create a blank dictionary

# dic = {"name":"prince sharma","Department":"data science"}

# print(dic)
# print(type(dic))


# car={"Brand":"BMW","Model":"Model-20","Year":"2024",
# "Color":"Red","Fuel":"Petrol"}

# print(len(car))

# a= car.keys()
# print(a)

# b= car["Brand"]
# print("Brand:- ",b)

# c=car["Fuel"]
# print("Fuel type:- ",c)


# car={"Brand":"BMW","Model":"Model-20","Year":"2024",
#  "Color":"Red","Fuel":"Petrol"}


# x = str(input("Enter key:- ")).title()
# print(car[x])

# x={1:"simran",2:"ansh"
# ,3:"anshu",4:"vishwas"
# ,5:"dolly",6:"manjeet"
# ,7:"sneha"}

# print(x)
# print(len(x))


#functions:- 
# 1. Keys():- it is used to store the keys from the dictionary.
# Keys cannot be duplicate but values can be.

# a=x.keys()
# print(a)
# print(type(a))

# 2. Values():- it shows the values from the dictionary.

# b=x.values()
# print(b)
# print(type(b))

# 3. Items():- it shows the list in tuple in key and values.

# c=x.items()
# print(c)
# print(type(c))
# 4. get():- it filters the values according to keys.

# d=x.get(4)
# print(d)


# How to add keys and values in dictionary

# x={"Bihar":"Patna","Uttar pradesh":"lucknow","Assam":"dispur"}
# print(x)


# add the values 
# "Kolkata":"west bengal"
# "Delhi":"new delhi"
# "Haryana":"chandigarh"

# Without function   
# x["Kolkata"]="West bengal"
# x["Delhi"]="New delhi"
# x["Haryana"]="Chandigarh"

# print(x)


# With function

# update():- with the help of update function you can add single 
# or multiple keys and values in dictionary

# x.update({"Assam":"dispur"})

# print(x)

#-------------------------------27 May,2024----------------------------------

#Add uncommon text from x and y

# x="python is a programming language"
# y="python is an object oriented programming language"
# z=[]

# x=x.lower()
# y=y.lower()
# x=x.split()
# y=y.split()


# for i in x:
#     if i not in y:
#         z.append(i)

# for i in y:
#     if i not in x:
#         z.append(i)


# z=" ".join(z)

# print(z)


# for i in x:
#     if i in y:
#         z.append(i)
# print(z)




# Create a dict based on student and his marks (add five students)

# x={"Vishwas":96,"Simran":15,"Manjeet":100,"Shashank":95,"Dolly":88}


# x.update({"suraj":45,"kishan":56})

# print(x)




# show the state and and capital with the help of user input?

#   state           =  capital
# x={"Andhra Pradesh" : "Amaravati",
# "Arunachal Pradesh" : "Itanagar",
# "Assam" : "Dispur",
# "Bihar" : "Patna",
# "Chhattisgarh" : "Raipur",
# "Goa" :   "Panaji",
# "Gujarat" :   "Gandhinagar",
# "Haryana" :   "Chandigarh",
# "Himachal Pradesh": "Shimla",
# "Jharkhand" : "Ranchi",
# "Karnataka" : "Bengaluru",
# "Kerala" :    "Thiruvananthapuram",
# "Madhya Pradesh" :    "Bhopal",
# "Maharashtra":    "Mumbai",
# "Manipur":    "Imphal",
# "Meghalaya": "Shillong",
# "Mizoram" :   "Aizawl",
# "Nagaland" : "Kohima",
# "Odisha" :    "Bhubaneswar",
# "Punjab" :    "Chandigarh",
# "Rajasthan" : "Jaipur",
# "Sikkim" : "Gangtok",
# "Tamil Nadu" :    "Chennai",
# "Telangana" : "Hyderabad",
# "Tripura" : "Agartala",
# "Uttar Pradesh" : "Lucknow",
# "Uttarakhand" :   "Dehradun", 
# "West Bengal" :   "Kolkata"}

# y = str(input("enter any state :-")).title()
# print(f"The Capital of {y} is : {x[y]}")



# x={"A":45,"F":56,"E":89,"B":50}

# print(x)

#1. popitem():- it is used to delete the key and values from the last
#2. pop():- it is used to delete the key and values according to keys.
#3. clear:- it is used to empty the dictionary
#4. del:- it is used to permanantly delete the dictionary

# a=x.popitem()
# print(x)

# x.pop("F")
# print(x)

# x.clear()
# print(x)

# del x
# print(x)


# create a dictionary with the help of user input

# x=int(input("Enter the length of dictionary:- "))
# d={}

# for i in range(x):
#     key=input("Enter the key:- ") 
#     val=input("Enter the value:- ")
#     d[key]=val

# print(d)

# x= {'vishwas': 56, 'manjeet': 77, 'shashank': 66}
# y={}

# z=x.items()
# for i,j in z:
#     y[j]=i

# print(x)
# print("---------------After the update--------------------")
# print(y)



# Sorting

#-------------------------------------------------


#sort the dictionary base of keys 
#in ascending order 

# x={1:"A",5:"C",4:"B",2:"R",6:"T"}
# #sorted in numeric order 
# y={}
# z=sorted(y)
# x=dict(z)
# print(x)

# sorted in alphabetic order
# y=x.items()
# z={}

# for i,j in y:
#     z[j]=i
# print(x)
# print(z)

# x=dict(sorted(z.items()))
# print(x)



# Sorting dictionary by keys 
# y=sorted(x.items(),key=lambda x:x[0])
# y=dict(y)

# print(y)


# x="Programming"

# # x="PrOgRaMmInG"
# y=len(x)
# for i in range(y):
#     if i%2==0:
#         print(x[i].upper(),end="")
#     else:
#         print(x[i].lower(),end="")

# find the minimum int in x
# x=[-1,-2,4,6,10]
#1.
# print(min(x))

#2.
# x=sorted(x)
# print(x[0])

# x="Programming"
# z=""
# y=len(x)
# for i in range(y):
#     if i%2!=0:
#         print(x[i].replace(x[i],"*"),end="")
        
#     else:
#         print(x[i],end="")
        

# print("-"*45)        
# print(str(z))

# for i in range(len(x)):
#     if i%2==0:
#         z+=x[i]
#     else:
#         z+="*"

# print(z)


# x=[2,8,12,6,10]

# x[0],x[-1]=x[-1],x[0]


# print(x)




# -----------         29 may 2024 -------------------
# --------------------------------------------------
# ---------------- NESTED DICTIONARY-------------
# -------------------------------------------------


# Nested Dict:- we use dict inside another dictionary 
# is called nestrd dictionary

# a = {"Name":"rohit","age":25,"city":"delhi"}
# b = {"Name":"raja","age":45,"city":"noida"}
# c = {"Name":"ram","age":21,"city":"Jaipur"}
# d = {"Name":"Virat","age":55,"city":"Chennai"}

# x = {1:a,2:b,3:c,4:d}

# print(x)

# # print("*"*70)

# print(x.keys())

# print(x.values())


# print(x[1]["age"])


# 1.show the values of rollno. 3

# print (x[3].values())
# 2.show the all keys of rollno.2

# print (x[3].keys())



# 3. show the city of virat.



# print(x[4]["city"])

# show all name of rollno.1



# print(x[1]["Name"])


# 4 show all keys og rollno.4
# print (x[4].keys())

# find the age of rollno 4 with get formula

# print(x[4].get("age"))


# a = {"Name":"rohit","age":25,"city":"delhi"}
# b = {"Name":"raja","age":45,"city":"noida"}
# c = {"Name":"ram","age":21,"city":"Jaipur"}
# d = {"Name":"Virat","age":55,"city":"Chennai"}


# x = {1:a,2:b,3:c,4:d}

# add marks in roll no.3

# x[3]["Marks"]=256

# print(x[3])

# x[2].update({"Marks":356,"state":"up"})
# print(x[2])



# x = {"car":{"Brand":["Kia","Honda","BMW"],
#           "Color":["red","Black","White"],
#           "Model":["BS6","BS4","BS6"],
#           "Year":[2015,2018,2016]},
#   "Bike":{"Brand":["Tvs","Bajaj","Hero"],
#           "Model":["A150","Pulser150","110"],
#           "Color":["red","black","white"],
#           "Year":[2019,2018,2020]}
# }

# print(x)

# a=x["car"]
# print(a)


# d=a["Brand"]
# print(d[-1])


# print(x["car"]["Brand"][-1])

# ----------------------------------------

# add fuel in bike   = ["petrol","CNG"]

# x["Bike"]["fuel"]=["petrol","CNG"]
# print(x)

# add color in bike green
# x["Bike"]["Color"].append("green")
# print(x["Bike"])


# x["car"].pop("Year")
# print(x["car"])


#----------------------30 May,2024-------------------------------------

##################### Python Project 1 ################################################
####################### Students Result ##########################################
# import time

# dic={ 
#      "Prince":{"maths":56,"sci":56,"sst":78,"eng":89,"hnd":75},
#      "Simran":{"maths":85,"sci":100,"sst":99,"eng":98,"hnd":97},
#      "Dolly":{"maths":89,"sci":58,"sst":36,"eng":38,"hnd":77},
#      "Mohit":{"maths":75,"sci":76,"sst":74,"eng":79,"hnd":73},
#      "Gulshan":{"maths":88,"sci":68,"sst":66,"eng":48,"hnd":87},
#      "Diya":{"maths":90,"sci":52,"sst":55,"eng":57,"hnd":41},
#      "Vansh":{"maths":74,"sci":47,"sst":25,"eng":22,"hnd":23},
#      "Nanu":{"maths":12,"sci":85,"sst":78,"eng":96,"hnd":89},
#        "Minny":{"maths":84,"sci":45,"sst":91,"eng":18,"hnd":56},
#        "Sumit":{"maths":59,"sci":50,"sst":30,"eng":30,"hnd":70},
#         "Prince":{"math":68,"sc":89,"sst":98,"eng":91,"hnd":75},
#         "Simran":{"math":87,"sc":89,"sst":43,"eng":90,"hnd":76},
#         "Parul":{"math":45,"sc":65,"sst":23,"eng":93,"hnd":78},
#         "Samrath":{"math":33,"sc":99,"sst":41,"eng":49,"hnd":77},
#         "Ram":{"math":34,"sc":35,"sst":36,"eng":37,"hnd":38},
#         "Preeti":{"math":42,"sc":44,"sst":46,"eng":54,"hnd":65},
#         "Anshu":{"math":21,"sc":96,"sst":67,"eng":12,"hnd":12},
#         "Anshumam":{"math":11,"sc":18,"sst":20,"eng":30,"hnd":39},
#         "Muskan":{"math":71,"sc":87,"sst":19,"eng":59,"hnd":44},
#         "Sumit":{"math":66,"sc":88,"sst":99,"eng":22,"hnd":83},
#         "Prince"  :{"Eng":88,"Hnd":80,"Mth":79,"Sci":67,"Sst":78},
#       "Yogesh"  :{"Eng":83,"Hnd":90,"Mth":69,"Sci":63,"Sst":68},
#       "Shashank":{"Eng":89,"Hnd":69,"Mth":83,"Sci":75,"Sst":87},
#       "Simran"  :{"Eng":88,"Hnd":80,"Mth":79,"Sci":67,"Sst":78},
#       "Vishwas" :{"Eng":76,"Hnd":67,"Mth":89,"Sci":73,"Sst":77},
#       "Ansh"    :{"Eng":83,"Hnd":84,"Mth":75,"Sci":66,"Sst":71},
#       "Dolly"   :{"Eng":81,"Hnd":89,"Mth":74,"Sci":87,"Sst":73},
#       "Manjeet" :{"Eng":78,"Hnd":70,"Mth":69,"Sci":61,"Sst":88},
#       "Kshitij" :{"Eng":84,"Hnd":79,"Mth":75,"Sci":84,"Sst":83},
#       "Harsh"   :{"Eng":80,"Hnd":82,"Mth":70,"Sci":62,"Sst":73},
#       "Prince":{"maths":56,"science":73,"sst":78,"eng":65,"hnd":75},
#     "Vishwas":{"maths":65,"science":73,"sst":80,"eng":75,"hnd":56},
#     "Dolly":{"maths":75,"science":66,"sst":54,"eng":69,"hnd":52},
#     "Aman":{"maths":50,"science":60,"sst":40,"eng":63,"hnd":71},
#     "Simran":{"maths":55,"science":56,"sst":60,"eng":53,"hnd":65},
#     "Ansh":{"maths":40,"science":59,"sst":68,"eng":71,"hnd":69},
#     "Annu":{"maths":56,"science":73,"sst":70,"eng":60,"hnd":74},
#     "Gurveer":{"maths":60,"science":70,"sst":73,"eng":67,"hnd":50},
#     "Parmod":{"maths":52,"science":55,"sst":78,"eng":66,"hnd":45},
#     "Sahil":{"maths":50,"science":45,"sst":61,"eng":56,"hnd":78},
#     "Prince":{"Maths":56,"Science":66,"SST":74,"English":89,"Hindi":75},
#     "Shashank":{"Maths":86,"Science":56,"SST":78,"English":83,"Hindi":95},
#     "Vishwas":{"Maths":46,"Science":86,"SST":38,"English":93,"Hindi":65},
#     "Dolly":{"Maths":56,"Science":46,"SST":71,"English":73,"Hindi":55},
#     "Simran":{"Maths":76,"Science":36,"SST":75,"English":84,"Hindi":45},
#     "Harmeet":{"Maths":46,"Science":46,"SST":79,"English":43,"Hindi":63},
#     "Manjeet":{"Maths":82,"Science":56,"SST":85,"English":82,"Hindi":35},
#     "Sneha":{"Maths":66,"Science":51,"SST":98,"English":53,"Hindi":73},
#     "Yogesh":{"Maths":46,"Science":56,"SST":78,"English":83,"Hindi":95},
#     "Ansh":{"Maths":69,"Science":80,"SST":72,"English":88,"Hindi":75}
# }



# # print(dic)

# name= input("Student Name:-").title()
# # print(dic[name])

# d=dic[name] # passing the parameter of each student by user input   

# marks=d.values()  # shows the all values of each student 

# marks=sum(marks)   # it shows total obtained marks

# per=marks/5  # percentage

# per2= str(round(per,1)) +"%"

# # print(per2)


# #-----------------------------------------------
# # Applying the division
# #-----------------------------------------------

# if per>=60:
#     div="First division"
# elif per>=45:
#     div="Second division"
# elif per>=33:
#     div="Third division"
# else:
#     div="Fail"
# #-------------------------------------------------

# print("-"*140)
# time.sleep(1)
# print("Full Marks:- ",500)
# print("-"*70)
# time.sleep(1)
# print("Obtained marks:- ",marks)
# print("-"*70)
# time.sleep(1)
# print("Percentage:- ",per2)
# print("-"*70)
# time.sleep(1)
# print("Division:- ",div)
# print("-"*70)



#------------------------------------3 June,2024-------------------------------------------
#------------------------------------------------------------------------------------------


# dic={"Shashank":{"Eng":89,"Hnd":69,"Mth":83,"Sci":75,"Sst":87},
#       "Simran"  :{"Eng":88,"Hnd":80,"Mth":79,"Sci":67,"Sst":78},
#       "Vishwas" :{"Eng":76,"Hnd":67,"Mth":89,"Sci":73,"Sst":77},
#       "Ansh"    :{"Eng":83,"Hnd":84,"Mth":75,"Sci":66,"Sst":71},
#       "Dolly"   :{"Eng":81,"Hnd":89,"Mth":74,"Sci":87,"Sst":73}
#     }

# while True:
#     r=int(input("Enter Your Roll Number:- "))
#     roll_no={1:"Shashank",2:"Simran",3:"Vishwas",4:"Ansh",5:"Dolly"}

#     x=roll_no[r]

#     y=dic[x]
#     v=sum(y.values())

#     per=v/5

#     if per>=60:
#         div="First Division"
#     elif per>=45:
#         div="Second Division"
#     elif per>=33:
#         div="Third Division"
#     else:
#         div="Fail"
#     print("-"*60)
#     print("Total Marks : ",500)
#     print("-"*60)
#     print("Obtained Marks: ", v )
#     print("-"*60)
#     print("Percentage of Marks: ",per,"%")
#     print("-"*60)
#     print("Division of Student: ",div)
#     print("-"*60)

#     var=int(input("Enter 1 to continue\n Enter any key to exit: "))

#     if var==1:
#         continue
#     else:
#         break


# Functions

# What is function?
# a function is a back of code which is only runs when it is called.
# You can pass data ,known as parameter,into a function.
# a function can return data as result.

# Creating a function in python 
# function is defined using the def keyword:

# There are mainly two functions :-

# 1. User defined function - the user defined function user perform the specific task.

# 2. Built in function - the built in function are those function that are predefined
 # in python ex:- sum min max sorted len type


# #Creating a function 
# def greet():
#     #greeting
#     print("Hello World")
# # #calling the function
# greet()



# def vishwas(x):
#     s=0
#     for i in x:
#         s+=i
#     print("Total sum of numbers:- ",s)

# y=[345,6,53,75,45,6,554,46]

# x=(23,64,86,24,43,85)

# vishwas(y)
# vishwas(x)


# def abc(x,y):
#     z=x+y
#     print(z)

# #calling the function 

# x=45
# y=10
# abc(x,y)


# Create a function to find the cube value of any number 
#with the help of user input

# def cube(x):
#     print(x**3)

# x=int(input("Enter the number:- "))
# cube(x)


# Create a function to show the last 3 alphabet of any text

# def last3(x):
#     print(x[-3:])

# x=str(input("Enter any text:- "))
# last3(x)


# Create a function to print who is eligible for vote or not


# def vote(x):
#     if x>=18:
#         print("Yes!!!!!!!!!!!!!!!!!")
#     else:
#         print("Not!!!!!!!!!!!!!!!!!")

# x=int(input("Enter the age of voter:"))
# vote(x)


# Create a function to calculate the avg of any number 

# def avg(x):
#     s=sum(x)
#     l=len(x)
#     print("Average :- ",s/l)

# a=[2,4,6,3,6,4]
# avg(a)

# Create a function to show the first 2 alphabet and last 2 alphabet in 
# capital letter and reset alphabets in small letter.


# def vishwas(x):
#     a=x[0:2].upper()
#     b=x[-2:].upper()
#     l=len(x)-4
#     c=x[2:l+2]

#     print(a+c+b)


# z="Narendra"
# vishwas(z)


#---------------------------------5 June,2024--------------------------------------------------



#1 Create a function to print the 2nd highest number from the list 

# def large2(x):
#     x.sort()
#     return x[-2]

# x=[34,45,23,56,3,95,13]

# print(large2(x))


#2 Create a function to show the index of second repititive alphabet from string


# def find2(a,b):
#     x=a.lower()
#     f=x.find(b)+1
#     f2=x.find(b,f)
#     print(f2)

# x="RAmayana"

# find2(x,"a")


# def st(x,y,z="Patna"):
#     print(f"Hello {x},\nMy Name is {y}\nI live in {z}")


# x="Good Morning"
# y="Vishwas"
# z="delhi"
# st(x,y,z)

# ---------------------------------6 June,2024------------------------------------------

# parameter or arguments?
# the terms paramter and arguments can be usedd for the same thing 
# information that are passed inti the function


# Arbitatry arguments, *args
# If you dont know how many arguments that will be passed into your function,
# add astrick * before the perameter name in the function definition


#Example1
# def abx(*x):
#     print("Welcome to ",x[0])
#     print("My name is ",x[1])
#     print("Python cost is ",x[2])

# abx("Python","Vishwas",4536)

#Example2
# def abd(x,*y):
#     print(x)
#     print(y[0])
#     print(y[1])

# abd("Helloo","Welcomee too","Python")



# Keyword Arbitatry arguments, **kwargs
# If you dont know how many arguments that will be passed into your function,
# add two astrick ** before the parameter name in the function definition.

#this way the function will receive a dictionary of arguments , and can access the items
#accordingly

#if the number of keyword arguments is known, add a double ** before the parameter 
#name

# def x(**a):
#     print("my name is" ,a["name"])
#     print("I study in class",a["Class"])
#     print("My age is ",a["Age"],"year")



# #Calling the function
# x(name="prince",Age=20,Class="xth")


# create a function to delete the last 3 value from the list.

# def del3(x):
#     del x[-3:]
#     return x

# x=[1,3,5,2,5,3,6,7,4,2]
# print(del3(x))



# create a function to capitalize each text from the list.

# def cap(x):
#     y=[]
#     for i in x:
#         y.append(i.title())
#     return y
# a=["prince","vishwas","harsh","manjeet"]

# print(cap(a))

# create a function to calculate all the arthemetric operation on two number.

# def cal(x,y):
#     return x-y,x*y,x/y,x**y,x%y,x//y

# a=cal(4,7)
# print(a)



### LAMBDA FUNCTION ###

# su= lambda x,y:x+y
# print(su(3,7))

#----------------------------10 June 2024------------------------------------------


#EXCEPTION handling:- when an errors occurs, or exception as we call it,python will normally stop generate an error
# messege.
# these exception can be handle using  the try statement:
# the try block lets you test a block of code for errors.
# the ecpect  block lets you handle the error.
# the else block lets you execute code when there is no error.
# the finally block lets you executebcode ,regardless of the result of the try- and except block

# try:
#   x=int(input("enter the number:-"))
#   if x%2==0:
#       print("even number")
#   else:
#       print("odd number")
# except:
#   print("please enter the number only")


# write a python program to show the values base of user input by index?
# exception:= please enter the number less then the lenght text.
# try:
#   x="dolly"
#   y = int(input("enter the index number :- "))
#   print(x[y])
# except:
#   print("-"*45)
#   print("please enter the number less then the lenght text")
#   print("-"*45)


# try:
#   x=10
#   y=5
#   print(y/x)
# except:
#   print("zerodivisionerror :division by zero")
# else:
#   print("code is working properly")
# finally:
#   print("done")


# try:
#   x=0
#   y=5
#   print(y/x)
# except:
#   print("zerodivisionerror :division by zero")
# else:
#   print("code is working properly")
# finally:
#   print("done")

# write the python program to find the sum of odd number and sum of all even number
# from 1 to 20
# in execption handling
# a=0
# x=1
# y=20
# b = 0
# while x>y:
#   if y%2==0:
#       a+=y
#   else:
#       b+=y
#   y+=1
# print(a)
# print(b)

# try:
#   e=0
#   o=0
#   for i in range(1,21):
#       if i%2==0:
#           e+=i
#       else:
#           o+=i
#   print("sum of odd number:-",o)
#   print("sum of even number",e)
# except:
#   print("check the code")
# else:
#   print("code is correct")
# finally:
#   print("done")




# Create a function to print even number with the help of user input 


# x=int(input("Enter the input:-"))
# for i in range(1,x*2+1):
#     if i%2==0:
#         print("Even numbers=",i)
#     else:
#         continue

# Create a new list show the data type of all value that is given in the list.

# x=["ram",45,"mamta",45.4,True,21j]
# y=[]
# for i in x:
#     y.append(type(i))
# print(y)


# print all the numerical data from the list

# x=["ram",45,"mamta",45.4,True,21j]

# for i in x:
#     if type(i)==int:
#         print(i)


# Convert a nested list to simple list

# x=[[[[12,45,[89,[18,21],22],78]]]]

# x=str(x)

# x=x.replace("[","")
# x=x.replace("]","")
# x=x.split(",")
# # print(x)
# y=[]
# for i in x:
#     y.append(int(i))

# print(y)

#--------------------------------11 June,2024------------------------------


#----------------------------------- OOPS ---------------------------------



# OOPS:- object oriented programmings

# A class is like a blue print which is used to create an object

# Class
# Object
# Methods
# Inheritance
# Polymorphism
# Data abstraction
# Encapsulation


# class calc:
#     def add(self,a,b):
#         self.a=a
#         self.b=b
#         return a+b

#     def sub(self,c,d):
#         self.c=c
#         self.d=d
#         return c-d


# x=calc()

# a=34
# b=63
# m=x.add(a,b)
# print("Addition:",m)

# n=x.sub(89,34)
# print("Substraction:",n)




# class show:
#     def sqr(self,a):
#         self.a=a
#         return a**2

#     def rem(self,b,c):
#         self.b=b
#         self.c=c
#         return b%c

#     def pri(self):
#         return "Honesty is the best policy"



# x=show()
# a=5
# sq=x.sqr(a)
# print("Square:",sq)

# re=x.rem(16,3)
# print("Reminder:",re)

# print(x.pri())




# __init__ function:- it is used to initialize all the classes 
# 


# class student:
#     def st(self,name,age):
#         self.name=name
#         self.age=age

# x=student()

# x.st("Tonny",45)

# print("Name: ",x.name)
# print("Age: ",x.age)


# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# x=student("Tonny",45)

# print("Name: ",x.name)
# print("Age: ",x.age)


#-------------------------------13 June,2024-------------------------------------------------




# class A:
#     def st(self):
#         print("Hello world!")

# class B:
#     def st2(self):
#         print("Object oriented programming")

# x=A()
# x.st()

# y=B()
# y.st2()


# ---------------------INHERITANCE---------------------------- 

#

###### SINGLE INHERITANCE ########


# class A:
#     def st(self):
#         print("Hello world!")

# class B(A):
#     def st2(self):
#         print("Object oriented programming")


# y=B()
# y.st(),y.st2()


#Q1 Create an account class with 2 attribute - balance & Account number
#    and create a method for debit and credit and printing balance


# class Account:
#     def __init__(self,balance,Acc):
#         self.balance=balance
#         self.Acc=Acc
        

#     def debit(self,amount):
#         self.balance-=amount
#         print("Debit amount :- ",amount)

#     def credit(self,amount2):
#         self.balance+=amount2
#         print("Credit amount :- ",amount2)




# x=Account(5000,12345)
# # print("Account number:- ",x.Acc)
# # print("Your bank balance is :- ",x.balance)

# x.debit(2000)
# print("left balance:- ",x.balance)
# x.credit(10000)
# print("total balance:- ",x.balance)



###### MULTIPLE INHERITANCE ########

# class A():
#     def first(self,a,b):
#         self.a = a
#         self.b = b
#         return a+b

#     def second(self):
#         print("Welcom to Python ")

# class B(A):
#     def third(self,c,d):
#         self.c = c
#         self.d = d
#         return c*d

#     def forth(self):
#         print("object oriented")

# class C(B):
#     def fifth(self,e):
#         self.e = e
#         for i in range(1,11):
#             print(f"{e} X {i} = {e*i}")


#     def sixth(self):
#         print("Brillica")

# #---------------------------------------
# x = C()
# print(x.first(45,89))
# print(x.third(12,10))
# x.second()
# x.forth()
# x.fifth(7)
# x.sixth()



######## HYBRID INHERITANCE ##########

# class A():
#     def first(self,a,b):
#         self.a = a
#         self.b = b
#         return a+b

#     def second(self):
#         print("Welcom to Python ")

# class B():
#     def third(self,c,d):
#         self.c = c
#         self.d = d
#         return c*d

#     def forth(self):
#         print("object oriented")

# class C(A,B):
#     def fifth(self,e):
#         self.e = e
#         for i in range(1,11):
#             print(f"{e} X {i} = {e*i}")


#     def sixth(self):
#         print("Brillica")

# #---------------------
# x = C()
# print(x.first(45,89))
# print(x.third(12,10))
# x.second()
# x.forth()
# x.fifth(7)
# x.sixth()



##### DATA ABSTRACTION :- It is used for hiding the implentation details of a class
#                         and only showing the essential features to the user.


# from abc import ABC
# class main(ABC):
#     def IQOO(self):
#         pass


# class A(main):
#     def _init_(self,a,b):
#         self.a=a
#         self.b=b
#         self.c=a+b+a*b


# x = A(12,45)
# print(x.c) 

##### ENCAPSULATION :- Wrapping data and function into a single unit(object)





































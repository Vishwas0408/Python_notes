#-------------------------------------17 June,2024-----------------------

#-----------------------#########--NUMPY--#########--------------------------------

# What is NumPy?
# NumPy is a Python library used for working with arrays.

# It also has functions for working in domain of linear algebra, fourier transform,
# and matrices.

# NumPy was created in 2005 by Travis Oliphant. It is an open source project and 
# you can use it freely.

# Which Language is NumPy written in?
# NumPy is a Python library and is written partially in Python,
# but most of the parts that require fast computation are written in C or C++.

# NumPy stands for Numerical Python.
# For installing numpy 

# 1. type "pip install numpy" on cmd prompt
# 2. then type import numpy on sublime


# import numpy as np


# x=np.array([[[12,56,87,34]]])
# print(x)
# print(type(x))

# x=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x)

# x=[[1,2,3],[4,5,6],[7,8,9]]
# print(x)

# x=np.array((12,34,5,2,55))
# print(x)


# Creating 1 Dimension Array

# x=np.array([12,34,45,"science",21j])
# print(x)

# print(type(x))

# print(np.ndim(x))

# print(x.shape)

# print(x.dtype)

# powerfull array seq
# string   u64
# complex  complex128
# float    float64
# int      int64


# 2 dimenional array (2D array)

# x=np.array([[12,45,78,89]])
# print(x)
# print("Type :- ",type(x))
# print("Data type:- ",x.dtype)
# print("Number of Dimension :- ",np.ndim(x))
# print("Shape of Array :- ",x.shape)

# Create a three dimension array and include all data 

# x=np.array([[[12,45,78,89,"science",21j]]])

# #1. check the type of variable 


# print("Type :- ",type(x))


# #2. check the data type of array

# print("Data type:- ",x.dtype)

# #3. check the length of array

# print("Length of array:- ",len(x))

# #4. show the number of dimension

# print("Number of Dimension :- ",np.ndim(x))



# x=[[1,2,3,4],[8,9,10,11],[12,13,14,15]]

# ar=np.array(x)
# print(ar)

# # print("Shape of the matrix :- ",ar.shape)
# # print(np.ndim(ar))

# t=ar.shape
# print(f"There are {t[0]} Rows and {t[1]} Columns")


# x=np.array([[12,45,56,],[98,87,36]])

# print(x)


#Extract the values 

# 45
# print(x[0][1])

# # 36
# print(x[1][2])

# # 87
# print(x[1][1])

# # 12
# print(x[0][0])

# # 98
# print(x[1][0])


# # 12,45
# print(x[0][0:2])


# # 87,36
# print(x[1][1:3])

# # 45,56
# print(x[0][1:3])


# Indexing & Slicing

import numpy as np

# x = np.array([12,45,78,89,56,23])
# # Extract

# # 78
# print(x[2])
# # 56
# print(x[-1])
# # 12
# print(x[0])

# 3D array 

# x = np.array([[[12,45,78,56,23]]])

# # 45 
# print(x[0,0,1])
# #23
# print(x[0,0,-1])
# #[12,45,78,56,23]
# print(x[0,0,0:])
# # [45,78]
# print(x[0,0,1:3])



x=np.array([[[ [12,45,10],[96,63,52],[9,8,7] ]]])

# print(x)
# print(x.shape)
# print(np.ndim(x))



#[12,45,10]
# print(x[0,0,0])

# # [8,7]
# print(x[0,0,2,1:3])

# # [[12,45,10],[96,63,52]]
# print(x[0,0,0:2])

# #63
# print(x[0,0,1,1])

# #10
# print(x[0,0,0,2])

# #96
# print(x[0,0,1,0])

# #45
# print(x[0,0,0,1])

#[[12,45,10],[96,63,52],[9,8,7]]
# print(x[0,0,0:])


# # [10,45,12]
# print(x[0,0,0,0::-1])

# # [63,96]
# print(x[0,0,1,-2:-4:-1])

# #[12,10]
# print(x[0,0,0,0::2])

# # [9,7]
# print(x[0,0,2,0::2])

# #[7,8]
# print(x[0,0,-1,:-3:-1])




# ndmin = minmum number of dimension

# x=np.array([12,45,78,89],ndmin=5)
# # print(x)

# #Replace 

# # 45 to 100
# x[0,0,0,0,1]=(100)
# print(x)


# # 89 to 200
# x[0,0,0,0,-1]=(200)
# print(x)

# #12 to 100

# x[0,0,0,0,0]=(100)
# print(x)


#--------------------------------19 June,2024-----------------------------------------


##################### NUMPY FORMULAE #################################

# 1. Arrange
# 2. Reshape
# 3. Zero
# 4. One
# 5. Dtype
# 6. Astype
# 7. Full
# 8. Sum
# 9. Mean
# 10. Median 
# 11. Std
# 12 Variance 
# 13. Concatenate
# 14. Transpose or T
# 15. Argmin
# 16. Argmax
# 17. Flatten
# 18. Diagflat
# 19. Diag
# 20. Flip

#----------------------------------------------------------------------

# import numpy as np

# x=np.array([12,45,78,56],ndmin=10)
# print(x)


#Dtype= when u use this formula in array it is used to convert 
# the data type into another format


# x=np.array([12,45,78,234],dtype="f")  # float=f, string=str, integer=i


# Arrange function:- It is used to print the number in sequence according
# to range.

# x=np.arrange(starting,ending,step_size)

# x=np.arange(1,11)
# print(x)

# x=np.arange(1,20,3)
# print(x)
# print(type(x))
# print(x.dtype)
# print(np.ndim(x))
# print(len(x))
# print(x.shape)


# Creating dimension with arange function

# x=np.arange(1,11,dtype="float")
# print(x)

# y=np.array(x,ndmin=5)
# print(y)


# #print reverse number from 40 to 35

# x=np.arange(40,34,-1)
# print(x)



# Reshape:- It is used to convert from array to matrix with combination.


# x=np.array([2,4,5,8,9,6,3,2,1])
# print(x)

# y=x.reshape(3,3)
# print(y)

# x=np.arange(1,100,4)
# print(x)
# print(len(x))

# y=x.reshape(5,5)
# print(y)

# x= np.arange(1,9)
# print(x)

# y=x.reshape(2,2,2) #(no. of matrix, rows, column)
# print(y)



# Concatenate:- It is used to join the array.

# x=np.array([12,3,4,5,7])
# print(x)

# y=np.arange(10,15)
# print(y)

# z= np.concatenate((x,y))
# print(z)


# Transpose :- It is used to change the rows into column and vice versa 
# limitation of this function is it can't be used in one dimension array


# x=np.array(1,10)
# y=np.arange(10,20)

# x=np.array([[1,2,3],[4,5,6]])

# print(x)
# print("*"*30)
# print(x.transpose())

# x=np.array([np.arange(1,10)])
# print(x.transpose())



# c=0
# x=int(input("enter number:- "))

# for i in range(1,x+1):
# 	for j in range(1,x+1):
# 		if i*j==x:
# 			print(i,"X",j)
# 			c+=1
# 		else:
# 			continue
# print("Total no. of combinations:- ",c)



#--------------------------------20 June,2024-------------------------------------------

import numpy as np

# x=np.arange(10,20)
# print(x)

#ZEROS:-

# x=np.zeros((4,5))
# print(x)

# x=np.zeros((3,5,5))
# print(x)

#ONES:-

# x=np.ones((4,5),dtype="str")
# print(x)


#FULL:-

# x=np.full((4,5),10)
# print(x)



# RANDOM.RANDINT():- It is used to generate the random number 
# according to user 

# x=np.random.randint(1,10,5) 
# print(x)


# x=np.random.randint((100,200,50))
# print(x)



# LINSPACE():- It is used to generate the number in sequencely 
# in same distance according  to user

#x=np.linspace(1,10,10)
# print(x)

# x=np.linspace(1,2,100)
# print(x)

# x=np.array([[12,45,78,89],[10,20,30,40],[96,74,85,23]])
# print(x)



#FLATTEN:- It is used to reduce the dimension of array into one dimension

# x=x.flatten()
# print(x)




#DIAGFLAT:- It is used to convert the matrix into a matrix showing values diagonally.
#diagonal

# x=np.array([[1,2,3,4],[2,3,5,6]])

# a=np.diagflat(x)
# print(a)



# DIAG:- With the help of this function it extract the diagonal
# value of matrix into 1d array

# b=np.diag(a)
# print(b)




# FLIP:- It is used to reverse the array

# x=np.array([[12,45,78,56]]) 
# print(x)

# print(np.fliplr(x))   # flip from left to right
# print(np.flip(x))
# print(np.sort(x))     # ascending 


#------------------------------------------------------------------------
# MATHEMATICAL FUNCTIONS
#------------------------------------------------------------------------

# MEAN:- sum of all no. divided by total number 
# MEDIAN:- it shows the mid value 
# STD:-  it is a square root value of variance
# VARIANCE:- it shows the spread between the data point to mean value 

# x=np.array([12,45,89,56,23,18,40])

# print("Average values:- ",np.mean(x))

# print("Median:- ",np.median(x))

# print("Std:- ",np.std(x))

# print("Variance:- ",np.var(x))

# print("Sum of numbers:- ",np.sum(x))


# x=np.array([[[12,45,98],[34,23,67]]])


# x=x.flatten()

# for i in x:
# 	print(i)


#NDITER():- With the help of this function we can reduce the dimension of 
# array and iterate with loop

# for i in np.nditer(x):
	# print(i)











































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































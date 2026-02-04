# pip install numpy  
# numpy  : 
"""
1. matrix : multiplication  , addition  
2. array manupulation. 
3. data anaylsis 

"""
import numpy as np 

"""
a=np.array([1,2,3,4,5,6,7,8,9],dtype=float)
print(a)
print(a.shape)
print(a.ndim)  # number  of  dimnesion 
print(a.size)  # number of elements
print(a.dtype)
"""

# 2 d array  : 

"""a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a.shape)
print(a.ndim)  # number  of  dimnesion
print(a.size)  # number of elements
"""

# arange : 

"""a=np.arange(1,13)  #  from  0 to 9 
print(a)
print(a.reshape(3,4))

b= np.arange(1,13).reshape(2,2,3)  # 2 ==>  number of  matrix , 2 ==> row  ,  3 ==> col
print(b)

c=np.arange(1,33).reshape(2,2,2,4)
print(c)
"""
# slicing : 
# a= np.array([1,23,45,67,89,22,56,99])

# index number start  with  0    ==> pos  ==> l  to  r 
# neg index number   start  -1:  ==> r  to l 

"""
print(a[3])
print(a[-1])
print(a[3:5])  # 3 start  index  5 end index
print(a[2 :6 :2 ])  # 2 start  index  6 end index  2 step

print(a[ : :2]) 
print(a[ : :3])
print(a[ : : -2])
print(a[ : : -1])
"""

# 2d array  slicing  : 

a= np.array([[1,2,3,40],[4,5,6,50],[7,8,9,90],[10,11,12,130]])
"""
[
 [ 1  2  3 40]   ===> row index 0 
 [ 4  5  6 50]  ===> row index 1
 [ 7  8  9 90]  ===> row index 2
 [10,11,12,130] ===> row index 3

"""
"""print(a)
print(a[1])
print(a[1,2])
print(a[1:3])
print(a[1:3,0:3])  # 1:3  ==> row  1:3 ==>col
print(a[:,0:3])  # 1:3  ==> row  1:3 ==>col

print(a[1:3,  : : -1])
"""
"""
[
 [ 1  2  3 40]   ===> row index 0 
 [ 4  5  6 50]  ===> row index 1
 [ 7  8  9 90]  ===> row index 2
 [10,11,12,130] ===> row index 3
]

task :1 
    print ==> [[5,6],
                [8,9]]
task :2 
    print ==> [1 5 9 130]

task :3 
    print ==> [[1,40], 
               [10,130] ]
"""

# flatten : 


"""a= np.array([[1,2,3,40],[4,5,6,50],[7,8,9,90],[10,11,12,130]])

a1 =a.flatten()  #  its convert to 1d array 
a1[1] =99
print(a)
print(a1)
"""
# ravel : 

"""
a= np.array([[1,2,3,40],[4,5,6,50],[7,8,9,90],[10,11,12,130]])

a1=a.ravel()
a1[1] =99
print(a1)
print(a)
"""
# statistical analysis :

"""a= np.array([[1,2,3,40],[4,5,6,50],[7,8,9,90],[10,11,12,130]])
print(a)
print(a.sum())  # sum of all elements
print(a.sum(axis=0))  # sum of all col
print(a.sum(axis=1))  # sum of all row

print(a.mean())
print(np.median(a))
print(np.std(a))
"""
#  ex :  1 2 3 4 5 6 7 8 9 10
# ex : 1 2 3 40 4 5 6 50 7 8 9 90 10 11 12 130  ==> median = ?

# np.one () :

a=np.ones(10,dtype=int).reshape(2,5)
print(a)

# np.zeros () : 
"""b=np.zeros(10,dtype=int).reshape(2,5)
c=np.zeros(32,dtype=int).reshape(2,2,2,4)

print(b)
print(c)
"""
# full :

d=np.full((2,5),fill_value=100)
print(d)
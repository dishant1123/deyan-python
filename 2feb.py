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
a= np.array([1,23,45,67,89,22,56,99])

# index number start  with  0    ==> pos  ==> l  to  r 
# neg index number   start  -1:  ==> r  to l 

print(a[3])
print(a[-1])
print(a[3:5])  # 3 start  index  5 end index
print(a[2 :6 :2 ])  # 2 start  index  6 end index  2 step

print(a[ : :2]) 
print(a[ : :3])
print(a[ : : -2])
print(a[ : : -1])
 

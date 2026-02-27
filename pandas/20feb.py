# pandas :  ==> pip install pandas
"""
1. data cleaning  
2. duplicate , missing value  remove  
3. data  analysis
"""
import pandas as pd

# seris  : 
"""
s= pd.Series([13,25,738,94,35,16,57,88,99,110])
print(s)

s1= pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print(s1)
"""
# head , tail, sample , shape, size ,ndim, dtype, values, index, info : 

"""s =pd.Series({"maths ":99,"english ":100,"physics ":98,"chemistry ":95,"biology ":90,"history ":85,"geography ":80,"computer science ":75,"arts ":70,"music ":65})

print(s)
print(s.head(3))  # default first  5 rows 
print(s.tail())  # default  last 5 rows
print(s.shape)  # number of rows , number of columns
print(s.size)  # number of elements
print(s.ndim)  # number  of  dimension
print(s.dtype)
print(s.values)
print(s.index)
print(s.info())
print(s.sample(5))
"""

# loc , iloc : 

s1= pd.Series([10,20,30,40,50],index=["a","b","c","d","e"])

print(s1)
print(s1['a'])
print(s1[0])

print(s1.loc['a'])
print(s1.iloc[4])

print("at",s1.at['c'])
print("at",s1.at['e'])

print("iat",s1.iat[3])

print(s1['a' : 'c'])
print(s1[['a' , 'c']])

s1[0]=200
print(s1)

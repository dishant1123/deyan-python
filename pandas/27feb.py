import  pandas as pd

"""
df =pd.read_csv("mckinsey.csv")
print(df)
print(df.head())
print(df.tail())

print(df.shape)
print(df.size)
print(df.ndim)
print(df.dtypes)
print(df.values)
print(df.keys())
print(df.info())
print(df.sample(5))
"""

# selected columns : 

"""
df = df["year"]
df= df[["year","continent"]]

df = df['year']>2000
print(df)
"""

# create dataframe manually :

"""t1= pd .DataFrame([
    ["A",23,90000],
    ["B",25,80000],
    ["C",27,70000],
    ["D",22,60000]
],columns=["name","age","salary"])
print(t1)
"""
"""t2= pd.DataFrame({
    "name" :["ram","sita","rahul","harsh"],
    "age" :[23,25,27,22],
    "salary" :[90000,80000,70000,60000]
})
"""
# print(t2)

# operation on dataframe :rename  , add_new col ,drop 

"""
t2= t2.rename(columns={"name":"First_Name","salary":"Stipend"})
t2.rename(columns={"name":"First_Name","salary":"Stipend"},inplace=True)
t2['Gender'] =['M','F','M','M']
t2.drop(columns=['age'],inplace=True)
print(t2)
"""

# task  :1 
"""
in  mckinsey.csv ===> year +3   ==>1955   
"""

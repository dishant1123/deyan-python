import pandas as pd 

df =pd.read_csv("mckinsey.csv")
"""print(df.head())

# loc  :explicit index   
# iloc : implicit index

print(df.loc[0])
print(df.iloc[0])

print(df.loc[2:5])
print(df.iloc[2:5])  # end  pos  excluded . 

print(df.iloc[2:5,1:4])
print(df.loc[2:5,"year" :"continent"])

print(df.iloc[[1,4,6,7],[0,3,4]])
print(df.iloc[1:10:2])
print(df.iloc[-1])
print(df.loc[-1])  # error
"""

# year : 2002  information  print 

"""result =df.loc[df['year']==2002]
print(result)
"""

# task :1 
"""
year ==2001 , life expectancy ,gdp 
"""

# a=df.loc[df['year']==2007,['life_exp','gdp_cap']] 
# print(a)

# task  :2 
"""
year ==2003 , country =india ,  life expectancy , gdp
"""

"""a=df.loc[(df['year']==2002) & (df['country']=='India'),['year','country','life_exp','gdp_cap']]
print(a)
"""
# task :3 life_exp  >28 display  



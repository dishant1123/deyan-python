import pandas as pd
import numpy as np


# duplicates :  it returns a boolean seris indicating whether each row is duplucated or not.

"""
syntax : 
df.duplucated(subset=None,keep="first")
"""
"""
df =pd.DataFrame(
    {
        'a' :[1,2,2,3], 
        'b' :[4,5,5,7],
    }
)
"""
# print(df)
# print(df.duplicated())

# duplicate based  on column : 
"""
print(df.duplicated(subset='a'))
print(df.duplicated(subset=['a','b']))
"""

# remove  duplicates :

"""df_clean = df.drop_duplicates()
print(df_clean)

"""
df=pd.DataFrame([[0,1,2,np.nan,5],[2,0,1,5,np.nan],[5,0,1,np.nan,5],[2,0,1,np.nan,np.nan]])
df=df.drop_duplicates(subset=[1,2])
df=df.drop_duplicates(subset=[4])

df =df.dropna(thresh=2,axis=1)  # axis =1  ==> col  axis =0 row 
print(df)

print(df.shape)

# apply  function  : 

import pandas as pd

"""
df =pd.DataFrame({
    'name' :['john','peter','mary','tom','jerry'],
    'science':[78,69,67,66,66],
    'math':[67,59,78,45,76]
})

# print(df)

df['avg'] =df.apply(lambda x :(x['science'] + x['math'])/2,axis =1)
# print(df) 
"""
"""
    name  science  math   avg
0   john       78    67  72.5
1  peter       89    89  89.0
2   mary       67    78  72.5
3    tom       96    65  80.5
4  jerry       66    76  71.0
"""
"""def grade(x) :
    if x['avg'] >70 :
        return 'dict'
    elif x['avg'] >60 :
        return 'first'
    else :
        return 'second'
    
df['grade'] =df.apply(grade,axis =1)
print(df)
"""

# groupby  :

df =pd.DataFrame({
    'name' :['john','peter','mary','tom','jerry'],
    'department' :['IT','IT','HR','Finance','Finance'],
    'salary' :[50000,60000,40000,70000,90000],
    'city' : ['ahmedabad','ahmedabad','delhi','ahmedabad','delhi']
})

print(df)

# task :1 print department wise salary

"""
department_wise_salary =df.groupby('department')['salary'].sum()
print(department_wise_salary)
"""
# task :2 multiple aggregate function  : min salary  max ,avg

"""
department_wise_salary =df.groupby('department')['salary'].agg(['sum','min','max','mean'])
print(department_wise_salary)
"""
# task :3 group by with multiple column : 

department_wise_salary =df.groupby(['department','city'])['salary'].sum()
print(department_wise_salary)

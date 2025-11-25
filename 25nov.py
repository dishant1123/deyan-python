# csv file  : read write  append 

import csv   

# w mode  : 
"""with  open("deyaan.csv","w",newline='') as f :
    writer =csv.writer(f)
    writer.writerow(["name","age","gender"])
    writer.writerow(["hitansh","20","male"])
    writer.writerow(["deyaan","19","male"])
    writer.writerow(["rima","20","female"])
    writer.writerow(["jiyaan","20","male"])
    
"""

# r mode : 

"""
with  open("deyaan.csv","r",newline='') as f :
    # reader  =csv.reader(f)
    # for i in reader :
        # print(i)
    
    result =csv.DictReader(f)
    for i in result :
        print(i)
"""

# a mode :

"""
with  open("deyaan.csv","a",newline='') as f :
    writer= csv.writer(f)
    
    writer.writerow(["chiku","12","female"])  # append  only  one  row
    writer.writerow(["preksha","19","female"])
    
"""

# multiple  row  : 

rows =[
    ["kishore","20","male"],
    ["kabir","20","male"],
]
with  open("deyaan.csv","a",newline='') as f :
    writer= csv.writer(f)
    
    writer.writerows(rows)# append multiple  row  using writerows
        
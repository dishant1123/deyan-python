# line  plot  : 

import  matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

"""days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temparature = [36.6,37.5,38.2,38.4,38.6,39.0,39.1,39.3,39.4,39.5,39.7,40.0,40.1,40.2,40.4]

plt.plot(days,temparature,"k*-",linewidth =3,markersize =10,label ="Guj temperature")
plt.title("Guj temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.legend(loc=1)
plt.grid(color ='k',linestyle ='-',linewidth =1)
plt.show()
"""

# ex :2 bar  

classes = ['python','R','ML','AI','Datascience']

class1_students =[30 ,15,20,25,10]
class2_students =[20,25,30,15,10]
class3_students =[10,20,30,25,15]

class_index = np.arange(len(classes))

width =0.3 

plt.bar(class_index,class1_students,width,color ='g',label ="Class 1")
plt.bar(class_index,class2_students,width,color ='y',label ="Class 2")
plt.bar(class_index,class3_students,width,color ='r',label ="Class 3")

plt.xticks(ticks =class_index+width,labels=classes)
plt.title("Students in each class")

plt.xlabel('course')
plt.ylabel('number of students')
plt.legend()
plt.show()

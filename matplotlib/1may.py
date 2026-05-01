import matplotlib.pyplot as plt
"""
matplotlib :  

1. graph  : line  , bar  , pie  , scatter  , histogram  , boxplot  , heatmap  , contour  , 3d  plot
2. style  ,color 
"""
# ex :1  line graph : 
"""x= [1,2,3,4,5,6,7,8,9,10]
y=[35,38,39,20,40,41,45 ,48,44,42]
plt.plot(x,y,color ="red",linewidth =2,linestyle ="--",marker ="o",markersize =5)
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Daywise Temperature")
plt.show()

"""

# ex :2  bar graph :

x=['kabir','jiyan','deyaan','hitansh','harsh']
y=[78,67,90,85,60]

plt.bar(x,y,color ="red",width =0.5,edgecolor ="black",linewidth =2,align ="center")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students Marks")
plt.show()


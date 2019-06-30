#from matplotlib import pyplot as plt
#import numpy as np
#dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
#
#x_indexes = np.arange(len(dev_x))
#width = 0.25
#
#dev_y = [38496, 42000, 46752, 49320, 53200,
#         56000, 62316, 64928, 67317, 68748, 73752]
#plt.bar(x_indexes-width, dev_y,  width = width ,label = 'all developer')
#
#
##python dev salary age
#
#py_dev_y = [45372, 48876, 53850, 57287, 63016,
#            65998, 70003, 70000, 71496, 75370, 83640]
#plt.bar(x_indexes, py_dev_y, color = 'y', label = 'all python developer')
#
#
#
#
#javascript dev salary
#js_dev_y = [37810, 43515, 46823, 49293, 53437,
#            56373, 62375, 66674, 68745, 68746, 74583]
#plt.bar(x_indexes+width, js_dev_y, width = width   ,  label = 'all java scipt developer')
#
#
#
#
#
#plt.legend()
#plt.xlabel("ages")
#plt.ylabel("salary")
#plt.title("salary of developer in (USD)")
#
#plt.style.use('fivethirtyeight')
#plt.show()
n  = int(input())
marksheet = [[input(), float(input())] for _ in range(n)]

names =  []
marks = []
for j in marksheet:
    for i  in  len([j]):
        names.append[0]
        marks.append[1]
names.sort()
marks.sort() 
names.remove(names[0:3])
print(names)
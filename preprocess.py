import os,sys,math
import re
import numpy as np
import pandas
import sklearn

dirName=os.path.dirname(os.path.abspath(__file__))
dirData=dirName+'/BigData/data'
trainfile=dirName+'/BigData/trainLabels.csv'
file_list=os.listdir(dirData)
fh=open(trainfile,'r')
tempDict={}
# parse the train values
flag=0
for temp in fh:
	tvals=temp.split(',')
	if flag==0:
		flag=1
	else:
		tempDict[int(tvals[0])]=[float(l) for l in tvals[1:]]
# Print the dict value
print tempDict[1]
n=len(file_list)

#for i in range(n):
#	print 'regressor '+str(i+1)
	

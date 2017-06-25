def findNumberInstance(x,array):
	num=0;
	for i in range(0,len(array)):
		if(array[i]==x):
			num=num+1
	return num

m=[1,2,34,4,2,1,3,2,1,2,3,2,1,2,32,32,2]
print(findNumberInstance(2,m))

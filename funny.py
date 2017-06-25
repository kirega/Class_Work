from random import randint

def RSelect(array,ith):
	starti=0
	endi=len(array)
	if endi==1:
		return array[0]
 
	pivot_index=randint(starti,endi)
	p_index=partition(array,pivot_index)

	if(ith==p_index): 
		return array[p_index]
	if(ith < p_index):
		RSelect(array[:p_index],ith)
	if(ith > p_index):
		ith=ith-p_index
		RSelect(array[p_index:],ith) 
   
def partition(array,pivot_index):
	starti=0
	endi=len(array)
	index=starti

	pivot_value=array[pivot_index]
 
	for i in range(starti,endi):
		if(array[i] < array[pivot_index]):
			array[i],array[index]=array[index],array[i]
			index+=1
	array[pivot_index],array[index] = array[index],array[pivot_index]
	return (index)

x = [3,0,8,7,5,9]
y=RSelect(x,2)
print (y) 
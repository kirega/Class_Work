from random import randint
#This function takes in an array,the start index and the end index
#and calls reccursively the sorting function  
def randomizedquicksort(A,starti,endi):
	if starti < endi:
		random_pivot=randint(starti,endi)
		A[starti],A[random_pivot]=A[random_pivot],A[starti]

		p_index=partition(A,starti,endi+1)
		randomizedquicksort(A,starti,p_index - 1)
		randomizedquicksort(A,p_index + 1,endi)
		return A 
#This function takes in an array,the start index and the end index
#and returns the partition index of the array
#plus it does the heavy duty of sorting the array
def partition(A,starti,endi): 
  
	pivot_index=starti
	pivot_value=A[pivot_index]
	p_index=starti

	for i in range(starti,endi):
		if A[i] < pivot_value:
			p_index += 1
			A[i],A[p_index ]=A[p_index],A[i]
	
	A[starti],A[p_index]=A[p_index],A[starti]

	return (p_index)
 
array=[17,41,5,22,54,6,29,90,13,12,54,21,71,72,21]
print('Unsorted array is')
print(array) 
print("Sorted array is")
print(randomizedquicksort(array, 0 , len(array)-1))
  
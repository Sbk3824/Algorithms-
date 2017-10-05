# List to be in sorted order
# Example of Divide and Conquer
def binarySearch(list,n):
	first = 0
	last = len(list)-1
	found = False

	while first<=last and not found:
		mp = (first+last)//2
		if list[mp] == n:
			found =True
		else:
			if n < list[mp]:
				last = mp-1
			else:
				first = mp+1
	return found

list = [1, 4, 6, 10, 15, 17, 20]
print(binarySearch(list,15)) # True
print(binarySearch(list, 2)) # False
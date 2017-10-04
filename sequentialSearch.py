def SeqSearch(list, n):
	pos = 0
	found = False

	while pos < len (list) and not found:
		if list[pos] == n:
			found = True
		else:
			pos = pos+1

	return found

list = [18, 6, 9, 10, 15, 17]
print(SeqSearch(list, 10)) # Returns True

print(SeqSearch(list, 13)) # Returns False
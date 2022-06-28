def Remove_dup(l):
	f_list = []
	for num in l:
		if num not in f_list:
			f_list.append(num)
	return f_list
	

dup_list = [12,24,35,24,88,120,155,88,120,155]
print(Remove_dup(dup_list)[::-1])

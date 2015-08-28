arr1 = [5,2, 100]
arr2 = [3,8, 15]
l = 3
result = [ ]
i = 0 
while i < l:
	if arr1[i] < arr2[i]:
		res = arr1[i]
	else:
		res = arr2[i]
	result.append(res)
	i += 1
print result
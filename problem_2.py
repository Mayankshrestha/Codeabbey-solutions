x = 8
sum_list = [10, 20, 30, 40, 5, 6, 7, 8]
n = 0
while n < x:
	r = sum_list[0:n+1]
	n = n +1
	result = sum(r)
print result


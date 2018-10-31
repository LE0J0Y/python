a=[[2,3,4],[1,5,4],[7,3,4]]
b=[[7,4,5],[2,4,2],[9,4,5]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
	for j in range(len(a[0])):
		result[i][j]=a[i][j]+b[i][j]
for i in range(0,len(a)):
	print "\n"
	for j in range(0,len(a[0])):
		print result[i][j],	

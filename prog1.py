namelist=[]
n=input("Enter the number of names:")
for i in range (1,n+1):
	name=raw_input("Enter the name:")
	namelist.append(name)
oldname=raw_input("Enter the name to be removed:")
newname=raw_input("Enter the new name:")
for index,i in enumerate(namelist):
	if i==oldname:
		namelist[index]=newname
	        print namelist
l=input("Enter the index value to be deleted:")
index=l
del namelist[l]
print namelist
word=raw_input("Enter the name to be deleted:")
for i,index in enumerate(namelist):
	if (word==index):
		del namelist[i]
print namelist	

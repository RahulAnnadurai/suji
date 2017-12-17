a=input()
b=input()
odds=[]
even=[]
if(a.isnumeric()):
	a=int(a)
	if(b.isnumeric()):
		b=int(b)
		for i in range(a,b):
			if(i%2!=0):
				odds.append(i)
			else:
				even.append(i)
		print(odds)
		
	else:
		print("invalid")
else:
	print("invalid")

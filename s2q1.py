a=input()
b=input()
if(a.isnumeric()):
	a=int(a)
	if(b.isnumeric()):
		b=int(b)
		c=a**b
		print(c)
	else:
		print("not valid")
else:
	print("not valid")

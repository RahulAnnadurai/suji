a=int(raw_input("enter the number"))
b=int(raw_input(" \n enter the number"))
c=int(raw_input(" \n enter the number"))
if(a<b):
	if(b>c):
		print("b is greater")
	else:
		print("c is greater")
elif(a>b):
	if(a>c):
		print("a is greater")
	else:
		print("c is greater")
else:
	print("c is greater")

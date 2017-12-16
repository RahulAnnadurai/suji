a=input("Enter the number")
if(a.isnumeric()):
	a=int(a)
	if(a%2==0):
		print("the number is even")
	else:
		print("the number is odd")
	
else:
	print("invalid")
	

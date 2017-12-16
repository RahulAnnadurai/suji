a=input("Enter the number")
if(a.isnumeric()):
  a=int(a)
  if(a>0):
      print("The number is positive")
  elif(a==0):
      print("The number is zero")
  else:
      print("The number is negative")
else:
    print("Not a valid number")

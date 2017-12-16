n=input()
def func(x):
    a= x[::-1]
    return a
b=func(n)
if(b==n):
    print("palindrome")
else:
    print("not palindrome")
    

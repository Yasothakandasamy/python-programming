n=int(raw_input())
m=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(m==rev):
    print("it is a palindrome")
else:
    print("it is not a palindrome")

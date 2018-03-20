a=int(raw_input())
if((a%400==0)or(a%4==0)and(a%100!=0)):  	  
    print("it is a leap year")
else:
    print("it is not a leap year")

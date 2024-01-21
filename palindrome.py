n=int(input("enter the number "))
reverse=0
temp=n

while(n>0):
    i=n%10
    reverse=reverse*10+i
    n=n//10


if temp==reverse:
    print("Number is a palindrome")
else:
    print("number is not a palindrome")











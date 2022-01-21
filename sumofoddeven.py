n=int(input("enter the number : "))
evensum=0
oddsum=0
for i in range(n) :
    d=n%10
    if (n%2==0):
        evensum+=d
    else:
        oddsum+=d
    n=n//10
print(evensum,oddsum)
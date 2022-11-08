bi=int(input("Enter a binary number: "))
n=bi
a=0
d=0
while n>0:
    r=n%10
    d=d+(r*(2**a))
    a+=1
    n=n//10
print(d)

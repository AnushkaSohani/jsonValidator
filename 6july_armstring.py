n=int(input("ENter a number "))
m=n
x=n

i=0
while(x!=0):
    x=x//10
    i=i+1

res=0
while(m!=0):
    a=m%10
    res=a**i+res
    m=m//10

# print("res",res)
# print("n",n)

if(res==n):
    print("Armstrong number")
elif(res!=n):
    print("Not an Armstrong number")
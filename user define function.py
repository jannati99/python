def add(a,b):
    sum=a+b
    print(sum)

a=int(input())
b=int(input())
add(a,b)
#another code
def add(*element):
    sum=0
    for i in range(n):
        sum=sum+arr[i]
    print(sum)

arr=[]
n=int(input())
for i in range(n):
    data=int(input())
    arr.append(data)
add(arr,n)
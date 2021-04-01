n=int(input("Enter the number of element :"))
arr=[]
sum=0
for i in range(n):
    data=int(input())
    arr.append(data)
for i in range(0,n,2):
    sum=sum+arr[i]
print(sum)

result=list(filter(lambda x: x%2==0,arr))
print(result)

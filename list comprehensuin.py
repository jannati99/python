n=int(input())
arr=[]
for i in range(n):
    data=int(input())
    arr.append(data)
result=[i for i in arr if i%2==0]
print(result)

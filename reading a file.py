file=open("file code","r")
print(file.readable())

text=file.read()
print(text)

size=len(text)
print(size)

t=list(file.readline())
print(t)

text=file.readline()[0]
print(text)

file.close()
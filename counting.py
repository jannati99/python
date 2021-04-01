word=0
letter=0
digit=0
n=input()
for x in n:
    x=x.lower()
    if(x>='a' and x<='z'):
        letter=letter+1
    elif(x>='0' and x<='9'):
        digit=digit+1
    else:
        word=word+1
print(word+1)
print(letter)
print(digit)
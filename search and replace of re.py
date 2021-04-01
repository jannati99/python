import re

pattern=r"color"

text1="my favourite color is red, i love blue color"

text2=re.sub(pattern,"dislike",text1)
print(text2)

text1="my favourite color is red, i love blue color"

text2=re.sub(pattern,"dislike",text1,count=1)
print(text2)


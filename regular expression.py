# match,search,findall

import re
pattern=r"colour"
text="Red is a colour , I love red colour"
if re.match(pattern,text):
    print("Match")
else:
    print("Not Match")

if re.match(pattern,"colour Red is a colour , I love red colour"):
    print("Match")
else:
    print("Not Match")


if re.search(pattern,"colour Red is a colour , I love red colour"):
    print("Match")
else:
    print("Not Match")

print(re.findall(pattern,text))

match= re.search(pattern,text
                 )

if match:
    print(match.start())
    print(match.end())
    print(match.span())

else:
    print("False")
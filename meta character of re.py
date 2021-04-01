import re

# . using

pattern=r"colo.r"
if re.match(pattern,"coloar"):
    print("Match")
else:
    print("Not match")


pattern=r"colo..r"
if re.match(pattern,"coloarr"):
    print("Match")
else:
    print("Not match")

#  ^ using

pattern = r"^colo..r$"
if re.match(pattern, "coloarp"):
    print("Match")
else:
    print("Not match")

# * using

pattern = r"a*"
if re.match(pattern, "coloarr"):
    print("Match")
else:
    print("Not match")

pattern = r"(ab)*"
if re.match(pattern, "abloarr"):
    print("Match")
else:
    print("Not match")

pattern = r"(ab)*"
if re.match(pattern, "abcoabloarr"):
    print("Match")
else:
    print("Not match")

# + using

pattern = r"a+"
if re.match(pattern, "coloarr"):
    print("Match")
else:
    print("Not match")

pattern = r"a+"
if re.match(pattern, "aaoloarr"):
    print("Match")
else:
    print("Not match")

pattern = r"a+"
if re.match(pattern, "aaacoloarr"):
    print("Match")
else:
    print("Not match")

pattern = r"a+b"
if re.match(pattern, "abloarr"):
    print("Match")
else:
    print("Not match")

pattern = r"a+b"
if re.match(pattern, "coloabrr"):
    print("Match")
else:
    print("Not match")

# ? using

pattern = r"ice(-)?cream"
if re.match(pattern, "icecream"):
    print("Match")
else:
    print("Not match")

pattern = r"ice(-)?cream"
if re.match(pattern, "ice-cream"):
    print("Match")
else:
    print("Not match")

# {} using

pattern = r"a{1-3}$"
if re.match(pattern,"aaagfjytkgu"):
    print("Match")
else:
    print("Not match")

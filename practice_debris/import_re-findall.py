import re

string = "The ghost that says boo haunts the loo"
m = re.findall("[bl]oo", string, re.IGNORECASE)
print(m)

#other answer
o = re.findall(".oo", "The ghost that says boo haunts the loo")
print(o)

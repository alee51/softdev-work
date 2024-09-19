'''
DISCO:
- to add to a dictionary, use .update()
- for .rsplit(), need to specify a maxsplit, or else it will do the same as .split()
  - default value of maxsplit is -1
'''
import random
file = open('occupations.csv')
string = file.read()
arr = string.split("\n")[1:-2]
# print(string)
# print(arr)
d = {}
for i in arr:
    i_split = i.rsplit(",", 1)
    d.update({i_split[0]:float(i_split[1])})
# print(d)
d.update({"Ducky":0.2})
random.choices(list(d.keys()), weights = list(d.values()))
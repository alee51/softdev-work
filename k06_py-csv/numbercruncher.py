# Perplexed Pigs: Anastasia Lee, Nia Lam
# SoftDev
# K06 -- reads a csv file, builds a dictionary from it, conducts weighted random choice
# 2024-09-19
# time spent: 1.2 hours
'''
DISCO:
- new way to open and read files (lines 28-29) automatically closes the stream after it's done
- to add to a dictionary, use .update()
- for .rsplit(), need to specify a maxsplit (maximum number of splits)
  - default value of maxsplit is -1, which will achieve the same as .split()
- random.choices(<list>, <weights>) conducts weighted random choice
QCC:
- the python random module is pretty expansive!
HOW THIS SCRIPT WORKS:
1. opens and reads the csv file
2. splits the string with the file's contents by new lines, disregarding the first and last line
  - we now have a list of strings of the form "<occupation>,<percentage>"
3. creates a dictionary and adds an entry for each occupation-percentage pair
  - converts percentages to floats before storing
  - we added another occupation so that the total is 100%
4. chooses and prints a random occupation using random.choices()
  - list of occupations from keys of dictionary
  - list of weights from values of dictionary
'''
import random
# open and read the csv file
with open("occupations.csv", "r") as file:
    f = file.read()

# list of strings "<occupation>,<percentage>", disregard first and last lines
arr = f.split("\n")[1:-2]
# print(arr)

# dictionary with occupations as keys and percentages (converted to floats) as values
d = {}
for i in arr:
    i_split = i.rsplit(",", 1)
    d.update({i_split[0]:float(i_split[1])})
# print(d)
d.update({"Ducky":0.2}) # the total is only 99.8%, so we added an occupation!

# chooses a random occupation from the list of keys according to the associated weights in the list of values
random_occ = random.choices(list(d.keys()), list(d.values()))[0]
print(random_occ)
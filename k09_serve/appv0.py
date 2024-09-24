# Anastasia Lee
# SoftDev
# September 2024

import random
import csv
from flask import Flask
def randocc():

	# open and read the csv file
	with open("occupations.csv", "r") as file:
	    arr = list(csv.reader(file))[1:-2]
# print(arr)
# arr is a list of lists [<occupation>, <percentage>], disregard first and last lines

# dictionary with occupations as keys and percentages (converted to floats) as values
	d = {}
	for i in arr:
	    d.update({i[0]:float(i[1])})
	d.update({"Ducky":0.2}) # the total is only 99.8%, so we added an occupation!
# print(d)

# chooses a random occupation from the list of keys according to the associated weights in the list of values
	random_occ = random.choices(list(d.keys()), list(d.values()))[0]
	return random_occ
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    string = "Anastasia, Mark, Brian<br>" + randocc()
    return string

if __name__ == "__main__":      # true if this file NOT imported
                                # meaning that we're running app.py, not another program that imported app.py
    app.debug = True            # enable auto-reload upon code change
    app.run()

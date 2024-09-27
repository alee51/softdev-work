# Anastasia Lee
# AID: Anastasia, Ivan, Danny
# SoftDev
# Sep 2024

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
I predict that the home webpage will be unchanged, but the "/my_foist_template"
webpage will present an error because the function test_tmplt() will try to use
render_template without it being imported.

Q1:
http://localhost:5000/my_foist_template

Q2:
The first argument is the file name of the template
The second argument is the title of the webpage (referenced in the template)
The third argument is the list that is referenced in the template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DISCO:
- when you go to http://localhost:5000/my_foist_template, the elements of collection
are printed on new lines to the webpage titled "fooooo" (as predicted)
- {{ }} is used for variables
- <!-- ... --> is a block comment in html
QCC:
- does render_template() search through all the directories available, or does
it look for a folder called "templates"?
  - the first argument doesn't specify the "templates" folder
- what does {% %} signify?
- how does the template know to replace collection with coll if there is no {{ }}?
- the template uses the html version of a for loop
  - how does html coding work?
"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
# (log prediction before executing...)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: Can all of your teammates confidently predict the URL to use to load this page?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()

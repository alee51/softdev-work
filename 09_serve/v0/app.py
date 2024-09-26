# Anastasia Lee
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # initializes a Flask object

@app.route("/")                # routes the hello_world function to the home directory
def hello_world():
    print(__name__)            # prints the name of the venv in the terminal, before the prompt
    return "No hablo queso!"   # is printed on the website that runs when the program is run

app.run()                      # calls the run method on the app object

# same as the code from k08

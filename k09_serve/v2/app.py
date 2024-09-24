# Anastasia Lee
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go? this prints in the terminal every time you load the website
                                  # not sure why it prints '(__main__)'; where is __name__ set to __main__?
    return "No hablo queso!"

app.run()

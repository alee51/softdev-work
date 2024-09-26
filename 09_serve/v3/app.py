# Anastasia Lee
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   #where will this go? same as v2; printed to the terminal every time you load the website provided
    return "No hablo queso!"

app.debug = True                      # this causes the debugger to be active and a debugger PIN to be printed to the terminal, but we're not sure what that does
app.run()

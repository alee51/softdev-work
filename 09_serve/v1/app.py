# Anastasia Lee
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

# even though the 'print(__name__)' line was omitted, the venv still ran properly
# and '(<venv name>)' was still printed before the prompt in the terminal

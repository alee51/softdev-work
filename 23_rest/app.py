from flask import Flask
import urllib.request

app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def home():
    str = open('key_nasa.txt', 'r').read()
    with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + str) as response:
        html = response.read()
    return 

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()

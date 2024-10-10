# &: Anastasia Lee, Nia Lam, Naomi Lai
# SoftDev
# October 2024

import os
from flask import Flask, session, render_template, request

app = Flask(__name__)    #create Flask object

app.secret_key = os.urandom(32)

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("SESSION")
    print(session)
    # print("\n\n\n")
    # print("***DIAG: this Flask obj ***")
    # print(app)
    # print("***DIAG: request obj ***")
    # print(request)
    # print("***DIAG: request.args ***")
    # print(request.args)
    # print("***DIAG: request.args['username']  ***")
    # print(request.args['username'])
    # print("***DIAG: request.headers ***")
    # print(request.headers)
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    # print("\n\n\n")
    # print("***DIAG: this Flask obj ***")
    # print(app)
    # print("***DIAG: request obj ***")
    # print(request)
    # print("***DIAG: request.args ***")    #for GET requests
    # print(request.args)
    # print("***DIAG: request.args['username']  ***")
    # print(request.args['username'])
    # print("***DIAG: request.headers ***")
    # print(request.headers)

    # print("***DIAG: request.form ***")    # for POST requests
    # print(request.form)
    
    print("REQUEST COOKIES")
    print(request.cookies.get('username'))
    # username = request.cookies.get('username')
    # if (username )
    
    session['username'] = request.cookies.get('username')
    print("DIAG: session username")
    print(session['username'])
    return session['username']  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

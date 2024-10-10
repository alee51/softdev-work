# &: Anastasia Lee, Nia Lam, Dua Baig
# SoftDev
# October 2024

#the conventional way:
from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
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
    if (request.method == 'GET'):
        return render_template( 'response.html', username = request.args['username'] )
    elif (request.method == 'POST'):
        return render_template( 'response.html', username = request.form['username'] )
    return "Invalid request method"
    
    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

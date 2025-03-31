from flask import Flask, render_template, request #importing necessary components from flask (Install it using python -m pip install flask)


app = Flask(__name__) #initialising flask


@app.route("/") #defining the routes for the home() funtion (Multiple routes can be used as seen here)
@app.route("/home")
def home():
    return render_template("home.html") #rendering our home.html contained within /templates

@app.route("/account", methods=["POST", "GET"]) #defining the routes for the account() funtion
def account():
    usr = "<User Not Defined>" #Creating a variable usr
    if (request.method == "POST"): #Checking if the method of request was post
        usr = request.form["name"] #getting the name of the user from the form on home page
        if not usr: #if name is not defined it is set to default string
            usr = "<User Not Defined>"
    return render_template("account.html",username=usr) #rendering our account.html contained within /templates

def about():
    return render_template("about.html") #rendering our about.html contained within /templates
@app.route("/about") #defining the routes for the about() funtion
@app.route("/about/<name>") #defining the routes for the about() funtion
def about_name(name):
    return render_template("about.html", username=name)
@app.route("/about/<name>/<int:age>")
def about_name_age(name, age):
    return render_template("about.html", username=name, age=age)
@app.route("/contact")
def contact():
    return render_template("contact.html") #rendering our contact.html contained within /templates
@app.route("/contact/<name>")
def contact_name(name):
    return render_template("contact.html", username=name)
@app.route("/contact/<name>/<int:age>")
def contact_name_age(name, age):
    return render_template("contact.html", username=name, age=age)
@app.route("/services")
def services():
    return render_template("services.html") #rendering our services.html contained within /templates
@app.route("/services/<name>")
def services_name(name):
    return render_template("services.html", username=name)
@app.route("/services/<name>/<int:age>")
def services_name_age(name, age):
    return render_template("services.html", username=name, age=age)
@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html") #rendering our portfolio.html contained within /templates

if __name__ == "__main__": #checking if __name__'s value is '__main__'. __name__ is an python environment variable who's value will always be '__main__' till this is the first instatnce of app.py running
    app.run(debug=True,port=4949) #running flask (Initalised on line 4)

from flask import Flask, render_template

server = Flask('todolist')


@server.get("/") #/ root page (home)
def home():
    return render_template('home.html')

@server.get("/about")
def about():
    return render_template('about.html')

@server.get("/contact")
def contact():
    return render_template("contact.html")





#start the server
server.run(debug=True)
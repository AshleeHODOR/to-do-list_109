from flask import Flask, render_template, request, redirect, url_for

server = Flask('todolist')

todo_list = ["Clean cat litter", "Mail package", "Wash Bob"]


@server.get("/") #/ root page (home)
def home():
    return render_template("home.html", todo_list=todo_list)

@server.post("/add")
def add_todo():
    print("hello from /add")
    todo_item = request.form.get("todo")

    if todo_item:
        todo_list.append(todo_item)

    return redirect(url_for("home")) 


@server.get("/about")
def about():
    return render_template("about.html")

@server.get("/contact")
def contact():
    return render_template("contact.html")





#start the server
server.run(debug=True)
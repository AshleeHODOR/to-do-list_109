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

all_images = []

@server.get("/gallery")
def gallery():
    return render_template("gallery.html", all_images=all_images)


@server.post("/addImage")
def add_image():
    image_url = request.form.get("image")
    all_images.append(image_url)
    return redirect(url_for("gallery"))




#------------- ONLINE STORE -------------------------

all_products = []

all_products = [
    {
        "title": "Notebook",
        "price": 13, 
        "image": "https://m.media-amazon.com/images/I/71FBzLvptzL.jpg"   
    },
    {
        "title": "Stickers",
        "price": 7.99, 
        "image": "https://campandsmore.com/cdn/shop/files/8DA5E0A7-E3C6-4844-9B07-831DDC514DA4.jpg?v=1700751900&width=823" 
    },
    {
        "title": "Planner with Pen!",
        "price": 19.89, 
        "image": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcSrgmkifeQvA8CReq0a-oYhUCnmve9vEEpE8mCCElDyV0BqdV3JKdJkbYymgbtUFQ79R7dbU0WtZdUxQO3kr-6fQIzpkR--rp-zUOinVwIXxROk5xEgs_-mgYJ7upd-WyJeBUX6Nbk&usqp=CAc"   
    }, 
    {
        "title": "Puzzle",
        "price": 29.99, 
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7uzP5xYssgZ0n_-LJhLYPFmhskAmQj6HPWhkUr-9Sz3d7fkhyRFPNM-v3HQaCt2x2A78&usqp=CAU" 
    },
    {
        "title": "The Alchemist",
        "price": 17, 
        "image": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcSxm76Kh1Eq2A9ed2j9q3l2j4NvBe9Ad_DLrJPtsYaTlbleVdVwqLMXUuggX9eDqqFXub4Jt7GY1aulnIFF13ajABTZuPEdgaJKkvbKLP0m6GOxILSd_is1HgV3dF-0wOu1WkdbVGStig&usqp=CAc"
    },
    {
        "title": "Temporary tattoos",
        "price": 11.99, 
        "image": "https://m.media-amazon.com/images/I/81CpfWs1RQL._AC_UF1000,1000_QL80_.jpg" 
    },
    {
        "title": "Travis Kelce Bobblehead",
        "price": 34.98, 
        "image": "https://www.foco.com/cdn/shop/files/BHNFSMUTNENKCTK_p_2048x.jpg?v=1737683677"   
    },
    {
        "title": "Titanic DVD",
        "price": 34.98, 
        "image": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQZaIsmdalhcCzj36k_lprPSsiNltliBDU4caGrN3rc5StVvprjpcb6rwPd5LOgIIsdZmG7XnX6DQ0Xl7jYPnJn8FObfqDDJi7nAoWNu_pH&usqp=CAc"   
    },
    {
        "title": "Volkswagon Toy",
        "price": 13.13, 
        "image": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcTfvFTm27Dvsu6ctbwjEoIS4tpnxyZ21YoEQkyduumn4n6pgcKgoGs4jZ2y6uiCnvycLT7JAT5UmAD4fTg4LuRafbZLg_NS_VSqctOxwiFIiKr1_ShuJ9OjMA"
    },
]

@server.get("/catalog")
def catalog():
    return render_template("catalog.html", all_products=all_products)

@server.get("/cart")
def cart():
    return render_template("cart.html")


#---------------------------------------------------------



#start the server
server.run(debug=True)
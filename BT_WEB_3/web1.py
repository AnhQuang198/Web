from flask import *
from datetime import *
import mlab
from models.fooditem import fooditem

app = Flask(__name__)

mlab.connect()
new_food = fooditem()

# new_food.src = "https://www.w3schools.com/w3images/wine.jpg"
# new_food.title = "The Perfect Sandwich, A Real NYC Classic"
# new_food.description = "Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum."
#
# new_food.save()

@app.route('/')
def hello_world():
    return redirect(url_for('test1'))

#
# @app.route('/cssdemo')
# def cssdemo():
#     return render_template("cssdemo.html")
#
@app.route('/addFood', methods=["GET","POST"])
def addFood():
    if(request.method == "GET"):
        return render_template("addFood.html")
    if(request.method == "POST"):
        new_food = fooditem()
        new_food.src = request.form["source"]
        # new_food.image = request.files["image"]
        new_food.title = request.form["title"]
        new_food.description = request.form["description"]
        new_food.save()
        return render_template("addFood.html")

@app.route('/deletefood', methods=["GET","POST"])
def deletefood():
    if(request.method == "GET"):
        return render_template("deletefood.html")
    if(request.method == "POST"):
        new_food = fooditem.objects(title=request.form["title"]).first()
        if new_food is not None:
            new_food.delete()
            return render_template("deletefood.html")

@app.route('/updatefood', methods=["GET","POST"])
def updatefoot():
    if(request.method == "GET"):
        return render_template("updatefood.html")
    if (request.method == "POST"):
        new_image = fooditem.objects(title=request.form["title"]).first()
        if new_image is not None:
            new_image.src = request.form["source"]
            new_image.description = request.form["description"]
            new_image.save()
        return render_template("update_image.html")


food_list = [
    {
        "src" : "https://www.w3schools.com/w3images/sandwich.jpg",
        "title" : "The Perfect Sandwich, A Real NYC Classic",
        "description" : "Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum."
    },
    {
        "src" : "https://www.w3schools.com/w3images/steak.jpg",
        "title" : "Let Me Tell You About This Steak",
        "description" : "Once again, some random text to lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum."
    },
    {
        "src" : "https://www.w3schools.com/w3images/cherries.jpg",
        "title" : "Cherries, interrupted",
        "description" : "Lorem ipsum text praesent tincidunt ipsum lipsum."
    },
    {
        "src" : "https://www.w3schools.com/w3images/wine.jpg",
        "title" : "Once Again, Robust Wine and Vegetable Pasta",
        "description" : "Lorem ipsum text praesent tincidunt ipsum lipsum."
    }
]

@app.route('/test1')
def test1():
    return render_template("test1.html",food_list = fooditem.objects)


if __name__ == '__main__':
    app.run()

from flask import *
from datetime import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for("test1"))

# girl_list = [
#     {
#         "src" : "http://68.media.tumblr.com/6707567f4007a0ebb6e342f37692da0b/tumblr_of8kzf8gMp1qbd81ro1_1280.jpg",
#         "title" : "mua by Glow studio | 0165 483 8886 ♥",
#         "tags" : "A lot more at http://xkcn.info - Xinh Ko Chiu Noi ♥"
#     },
#     {
#         "src" : "http://68.media.tumblr.com/7111feb3f9b20cadb1fca92d4aaf62f9/tumblr_of8kz3Im0h1qbd81ro1_1280.jpg",
#         "title" : "12343 by Đinh Văn Linh ♥",
#         "tags" :    "A lot more at http://xkcn.info - Xinh Ko Chiu Noi ♥"
#     },
#     {
#         "src" :"http://68.media.tumblr.com/a599f62ef0b9c12f9170c117e4db7557/tumblr_ocb33pL9ch1qbd81ro1_1280.jpg",
#         "title" : "Mis Trang - Khánh Chi by minhdh1881 ♥",
#         "tags" :    "A lot more at http://xkcn.info - Xinh Ko Chiu Noi ♥"
#     }
# ]

food_list_fist = [
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

food_list_second = [
    {
        "src" : "https://www.w3schools.com/w3images/popsicle.jpg",
        "title" : "All I Need Is a Popsicle",
        "description" : "Lorem ipsum text praesent tincidunt ipsum lipsum."
    },
    {
        "src" : "https://www.w3schools.com/w3images/salmon.jpg",
        "title" : "Salmon For Your Skin",
        "description" : "Once again, some random text to lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum."
    },
    {
        "src" : "https://www.w3schools.com/w3images/sandwich.jpg",
        "title" : "The Perfect Sandwich, A Real Classic",
        "description" : "Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum."
    },
    {
        "src" : "https://www.w3schools.com/w3images/croissant.jpg",
        "title" : "Le French",
        "description" : "Lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum."
    }
]


@app.route('/cssdemo')
def cssdemo():
    return render_template("cssdemo.html")

@app.route('/w3cssdemo')
def w3cssdemo():
    return render_template("w3cssdemo.html")

@app.route('/test1')
def test1():
    return render_template("test1.html",food_list_fist = food_list_fist,food_list_second = food_list_second)

if __name__ == '__main__':
    app.run()

import os
from os import sep
from flask import Flask, render_template, session
import wikipedia
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jinja-fory")
def jinja_fory():
    lista=["11111", "222222", "33333", "44444"]
    return render_template("jinja-fory.html", jlista=lista)

@app.route("/jinja-ify")
def jinja_ify():
    nr=22
    return render_template("jinja-ify.html", jnr=nr)

@app.route("/test")
def test():
    ny = wikipedia.page("Maria Skłodowska-Curie")
    
    # *******************************************
    # zapisuje wszystkie linki do zdjęć na stronie
    if not os.path.exists("all_img_on_page.txt"): # jeżeli plik nie istnieje
    # if os.stat("all_img_on_page.txt").st_size == 0: # jeżeli plik jest pusty
        all_img_on_page = ny.images
        for image_url in all_img_on_page:
            if not image_url.endswith('.svg'):
                with open("all_img_on_page.txt", "a+") as f:
                    f.write(image_url + '\n')
            else:
                pass
    else:
        pass
    # *******************************************
    
    with open('all_img_on_page.txt', 'r') as f:
        test_img = random.choice(f.readlines())
    
    return render_template("test.html", test_img=test_img)

if __name__ == "__main__":
    app.run(debug=True)
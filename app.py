from flask import Flask, render_template, session

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

@app.route("/flaga")
def flaga():
    return render_template("flaga.html", photo=outf)

from lxml import html
import requests

url = 'https://en.wikipedia.org/wiki/Nicolaus_Copernicus'

tree = lxml.html.parse(url)
img = tree.get_element_by_id('img')
img_url = img.attrib['src']

with open('image.jpg', 'wb') as outf:
    data = requests.get(img_url).content
    outf.write(data)

if __name__ == "__main__":
    app.run(debug=True)
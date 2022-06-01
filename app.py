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

if __name__ == "__main__":
    app.run(debug=True)
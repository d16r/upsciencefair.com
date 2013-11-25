from flask import Flask, render_template
from flask_frozen import Freezer

import sys
import shutil

app = Flask(__name__)
freezer = Freezer(app)

########################################
############  App URLs  ################
########################################


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/introduction/")
def introduction():
    return render_template('introduction.html')


@app.route("/materials/")
def materials():
    return render_template('materials.html')


@app.route("/results/")
def results():
    return render_template('results.html')


@app.route("/conclusion/")
def conclusion():
    return render_template('conclusion.html')


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        shutil.rmtree('./build')
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', debug=True)

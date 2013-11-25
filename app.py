from flask import Flask, render_template

app = Flask(__name__)

########################################
############  App URLs  ################
########################################


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/introduction")
def introduction():
    return render_template('introduction.html')


@app.route("/materials")
def materials():
    return render_template('materials.html')


@app.route("/results")
def results():
    return render_template('results.html')


@app.route("/conclusion")
def conclusion():
    return render_template('conclusion.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

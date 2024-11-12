from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/question")
def question():
    return render_template('question.html')

@app.route("/no")
def no():
    return render_template('no.html')



@app.route("/yes")
def yes():
    return render_template('yes.html')


@app.route("/newHome")
def newHome():
    return render_template('newHome.html')
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


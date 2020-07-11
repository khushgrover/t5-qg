import flask
from flask import Flask, request, render_template
from question_generation.pipelines import pipeline

app = Flask(__name__)

nlp = pipeline("e2e-qg")

@app.route('/')
def hello_world():
    return render_template("question_generation.html")

@app.route("/predict",methods=['POST'])
def predict():
    sentence = str(request.form["text"])
    output=nlp(sentence)
    return render_template('question_generation.html',pred='{}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)

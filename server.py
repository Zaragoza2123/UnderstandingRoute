from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<x>')
def say_input(x):
    return f"Hi {x}!"

@app.route('/repeat/<int:y>/<w>')
def repeatition(y, w):
    for i in range(0,y):
        return f"{w}"

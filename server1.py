from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<str>')
def say_input(str):
    if str == "flask" or str == "michael" or str == "john":
        return f"Hi {str}!"
    else:
        return "Sorry! No response. Try Agian."

@app.route('/repeat/<int:y>/<str>')
def repeatition(y, str):
    if (y, str) == (35,"hello") or (y,str )== (80,"bye")  or  (y,str)  == (99,"dogs"):
        return y * f"<h1>{str}<h1>"
    else:
        return "Sorry! No response. Try Agian."


if __name__=="__main__":
    app.run(debug=True)
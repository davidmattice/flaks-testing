from flask import Flask, render_template

msg = "Hello World2"

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', msg=msg)

if __name__ == "app":
    msg="Bob"
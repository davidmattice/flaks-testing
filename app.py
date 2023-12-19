from flask import Flask, render_template, request

msg = "Hello World2"
enabled = 0

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    global enabled
    activate = None

    if request.method == 'POST':
        activate = request.form.get('activate')
        if activate == "enable":
            enabled = 1
        elif activate == "disable":
            enabled = 0

    return render_template('index.html', msg=msg, enabled=enabled)

if __name__ == "app":
    msg="Bob"
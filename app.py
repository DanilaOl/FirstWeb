from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['name'])
        return 'Form was sent'
    return render_template('index.html')


@app.route('/users/<name>')
def user_page(name):
    return render_template('user.html', name=name)


app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session
from model import add_user
from model import AccountExists


app = Flask(__name__)
app.secret_key = 'megapasswordnagibator'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        password_check = request.form['password_check']
        if password != password_check:
            return render_template('index.html', error='passwords_dont_match')
        try:
            add_user(name, email, password)
        except AccountExists:
            return render_template('index.html', error='account_already_exists')
        session['account'] = name
        return redirect('/users/' + name)
    return render_template('index.html')


@app.route('/users/<name>')
def user_page(name):
    return render_template('user.html', name=name)


@app.route('/logout')
def logout():
    session.pop('account', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

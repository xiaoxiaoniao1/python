from flask import Flask, request, session, render_template, redirect, url_for

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    if "username" in session:
        return render_template("index.html", username = session['username'])
    else:
        return redirect(url_for('login'))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/do_login", methods=['POST'])
def doLogin():
    username = request.form['username']
    password = request.form['password']

    if username == "admin" and password == "123":
        session['username'] = username
        return redirect(url_for('index'))

    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/sendmail', methods=('GET', 'POST'))
def sendmail():
    return render_template("mail.html")


@app.route('/decrypt', methods=('GET', 'POST'))
def decrypt():
    return render_template('decrypt.html')


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, url_for, request, flash, redirect
from sendmail import SendMail
from decrypt import Decrypt, key

app = Flask(__name__)
app.config["SECRET_KEY"] = "crypto"


@app.route('/sendmail', methods=('GET', 'POST'))
def sendmail():
    if request.method == 'POST':
        # get all the inputes
        receiver = request.form["receiver"]
        subject = request.form["subject"]
        body = request.form["mail_content"]
        # execute the sendmail function
        SendMail(receiver, subject, body)

        return redirect(url_for('sendmail'))
    return render_template("mail.html")


@app.route('/decrypt', methods=('GET', 'POST'))
def decrypt():
    if request.method == 'POST':
        try:
            # get all the inputes
            public_key = eval(request.form["public_key"])
            encrypted = eval(request.form["encrypted"])
            tag = eval(request.form["tag"])
            nonce = eval(request.form["nonce"])
            # execute the decrypt function
            Decrypt(key(public_key), encrypted, tag, nonce)
        except SyntaxError:
            flash("Invali Input", "error")
        except NameError:
            flash("Encryption Format Not Valid", "error")

    return render_template('decrypt.html')


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

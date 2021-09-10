from flask import Flask, render_template, redirect, request, session
from user import User
app = Flask(__name__)



@app.route("/")
def index():
    x = User.get_all()
    return(render_template('read_all.html', all_users = x))


@app.route("/newuser")
def newuser():
    return(render_template('create.html'))


@app.route('/create_user', methods =["POST"])
def createuser():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)


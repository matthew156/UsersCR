from flask import Flask, render_template, redirect, request, session
from user import User
app = Flask(__name__)



@app.route("/")
def index():
    return(render_template('read_all.html', all_users = User.get_all()))


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


@app.route('/useredit/<int:id>')
def edit(id):
    data ={
        "id":id
    }
    return render_template('edit_user.html', user=User.one_user(data))

@app.route('/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    data ={
        "id":id
    }
    User.delete(data)
    return redirect('/')

@app.route('/select/<int:id>')
def select(id):
    data ={
        "id":id
    }
    return render_template('select.html', user= User.select(data))



if __name__ == "__main__":
    app.run(debug=True)


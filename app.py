# Use those packages which we need and import it from Flask

from flask import Flask, render_template, request, redirect, session, flash, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from datetime import datetime
from database_manager import connection_URI

# Use Flask Secret Key
app = Flask(__name__)
app.secret_key = "Ali_Project"

# Setting up database connection
sql_server_URI = f"mssql+pyodbc:///?odbc_connect={connection_URI}Encrypt=no"
app.config["SQLALCHEMY_DATABASE_URI"] = sql_server_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
database = SQLAlchemy(app)


# This is the database table for Title and Description.
class Note(database.Model):
    serial_number = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(200), nullable=False)
    desc = database.Column(database.String(500), nullable=False)
    date_created = database.Column(database.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.serial_number} - {self.title}"


# This is the Database use for Login and SignUp Pages.
class User(database.Model):
    email = database.Column(database.String(150), primary_key=True)
    password = database.Column(database.String(70), nullable=True)


# Creating all the database tables
with app.app_context():
    database.create_all()


# This is HomePage Route
@app.route("/index", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        read = Note(title=title, desc=desc)
        database.session.add(read)
        database.session.commit()
        return redirect("/index")
    allRead = Note.query.all()
    for read in allRead:
        read.date_created = read.date_created.strftime("%d-%m-%y")
    return render_template("Page 1.html", allRead=allRead)


# This is the Route for move to the About Page.
@app.route("/about")
def About():
    return render_template("About.html")


# This is the Route for Logout Page.
@app.route("/logout", methods=["GET"])
def logout():
    if "user" in session:
        session.pop("user")
        flash("You have been Logged Out", "success")
        return redirect("/")
    else:
        return redirect("/index")


# This is the Route for Login Page.
@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                session["user"] = user.email
                flash("Login successful", "success")
                return redirect("/index")
            else:
                flash("Wrong Password, Please try again", "warning")
                return redirect("/")
        else:
            flash("Invalid Email, Password", "warning")
            return redirect("/")


# This is the Route for SignUp Page.
@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "GET":
        return render_template("Signup.html")
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        new_user = User(email=email, password=password)
        database.session.add(new_user)
        database.session.commit()
        flash("Account created successfully, Login Now", "success")
        return redirect("/")


# This is the Route for the Change Page.
@app.route("/change/<int:serial_number>", methods=["GET", "POST"])
def change(serial_number):
    if request.method == "POST":
        title = request.form.get("title")
        desc = request.form.get("desc")
        note = Note.query.filter_by(serial_number=serial_number).first()
        note.title = title
        note.desc = desc
        database.session.add(note)
        database.session.commit()
        return redirect("/index")
    note = Note.query.filter_by(serial_number=serial_number).first()
    return render_template("change.html", read=note)


def includes(substring: str, string: str) -> bool:
    return bool(substring in string)


# This is the Route for the Search Page.
@app.route("/search")
def search():
    search_input = request.args.get("searchInput")
    try:
        search_input_int = int(search_input.strip())
    except Exception as e:
        search_input_int = None
    queryResults = Note.query.filter(
        or_(
            Note.title.contains(search_input),
            Note.desc.contains(search_input),
            Note.serial_number == search_input_int,
        )
    )
    return render_template("search.html", results=queryResults)


# This is the Route for the Delete Page.
@app.route("/delete/<int:serial_number>")
def delete(serial_number):
    note = Note.query.filter_by(serial_number=serial_number).first()
    database.session.delete(note)
    database.session.commit()
    return redirect("/index")


# This is use for debugging the App and port changing
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)

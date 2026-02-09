from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]
students = db["students"]


@app.route("/")
def index():
    all_students = list(students.find())
    return render_template("index.html", students=all_students)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        roll = request.form["roll"]
        marks = request.form["marks"]

        students.insert_one({
            "name": name,
            "roll": roll,
            "marks": marks
        })

        return redirect("/")

    return render_template("add_student.html")


@app.route("/update", methods=["GET", "POST"])
def update_student():
    if request.method == "POST":
        roll = request.form["roll"]
        marks = request.form["marks"]

        students.update_one(
            {"roll": roll},
            {"$set": {"marks": marks}}
        )

        return redirect("/")

    return render_template("update_student.html")


@app.route("/delete/<roll>")
def delete_student(roll):
    students.delete_one({"roll": roll})
    return redirect("/")


@app.route("/search", methods=["GET", "POST"])
def search_student():
    student = None

    if request.method == "POST":
        roll = request.form["roll"]
        student = students.find_one({"roll": roll})

    return render_template("search_student.html", student=student)

@app.route("/students")
def show_students():
    all_students = list(students.find())
    return render_template("show_students.html", students=all_students)



if __name__ == "__main__":
    app.run(debug=True)


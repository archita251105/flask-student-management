from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Archita", "course": "Python"},
    {"id": 2, "name": "Ryzen", "course": "Flask"},
    {"id": 3, "name": "Ananya", "course": "Web Development"}
]


@app.route("/")
def home():
    title = "Flask Jinja2 Demo"
    username = "Student"
    is_logged_in = True

    return render_template(
        "index.html",
        title=title,
        username=username,
        is_logged_in=is_logged_in,
        students=students
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/go-home")
def go_home():
    return redirect(url_for("home"))


@app.route("/form", methods=["GET", "POST"])
def form():
    error = None
    success = None

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:
            error = "Both name and email are required."
        elif "@" not in email:
            error = "Please enter a valid email address."
        else:
            success = f"Form submitted successfully by {name}!"

    return render_template("form.html", error=error, success=success)


@app.route("/api/students")
def api_students():
    return jsonify(students)


if __name__ == "__main__":
    app.run(debug=True)
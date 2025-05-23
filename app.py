import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)  # ← Flaskアプリ定義は最初に！

@app.route("/")
def universities():
    universities = os.listdir("data")
    return render_template("universities.html", items=universities)

@app.route("/<univ>")
def faculties(univ):
    path = os.path.join("data", univ)
    faculties = os.listdir(path)
    return render_template("faculties.html", univ=univ, items=faculties)

@app.route("/<univ>/<faculty>")
def departments(univ, faculty):
    path = os.path.join("data", univ, faculty)
    departments = os.listdir(path)
    return render_template("departments.html", univ=univ, faculty=faculty, items=departments)

@app.route("/<univ>/<faculty>/<department>")
def years(univ, faculty, department):
    path = os.path.join("data", univ, faculty, department)
    years = os.listdir(path)
    return render_template("years.html", univ=univ, faculty=faculty, department=department, items=years)

@app.route("/<univ>/<faculty>/<department>/<year>")
def exams(univ, faculty, department, year):
    path = os.path.join("data", univ, faculty, department, year)
    files = os.listdir(path)
    return render_template("exams.html", files=files, path=f"/pdf/{univ}/{faculty}/{department}/{year}")

@app.route("/pdf/<univ>/<faculty>/<department>/<year>/<filename>")
def serve_pdf(univ, faculty, department, year, filename):
    path = os.path.join("data", univ, faculty, department, year)
    return send_from_directory(path, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
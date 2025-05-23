from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    files = ["2023-ディジタル制御システム.pdf"]
    return render_template("index.html", files=files)

@app.route("/view/<filename>")
def view_pdf(filename):
    return render_template("viewer.html", filename=filename)

@app.route("/pdf/<filename>")
def serve_pdf(filename):
    return send_from_directory("data", filename)

if __name__ == "__main__":
    app.run(debug=True)
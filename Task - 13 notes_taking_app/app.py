from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
@app.route('/',methods=["GET","POST"])
def home_page():
    note = request.form.get("note")
    notes.append(note)
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
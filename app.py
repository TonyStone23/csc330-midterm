from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        todos.append(task)
        return redirect("/")
    
    return render_template("index.html", todos=todos)

if __name__ == "__main__":
    app.run(debug=True)

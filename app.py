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


@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
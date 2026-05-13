from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = ["Learn Git", "Build Docker image", "Run Terraform"]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template("index.html", tasks=tasks)

@app.route("/api/tasks")
def api_tasks():
    return jsonify({"tasks": tasks})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
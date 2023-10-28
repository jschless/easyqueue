import queue

from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


class BasicQueue(list):
    def push(self, i):
        self.insert(len(self), i)

    def pop(self):
        return super().pop(0)


queue = BasicQueue()


@app.route("/")
def home() -> str:
    return render_template("waiting_room.html", queue=queue)


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    queue.push(name)
    return home()


@app.route("/next", methods=["GET"])
def next():
    person = queue.pop()
    print(f"Seeing {person} now")
    return home()

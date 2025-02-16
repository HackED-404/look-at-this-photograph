from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def foo(picture):
    # Placeholder for the actual implementation of foo
    return f"bar"


@app.route("/upload", methods=["POST"])
def upload_picture():
    if "picture" not in request.files:
        return "No picture part in the request", 400
    picture = request.files["picture"]
    result = foo(picture)
    return result


if __name__ == "__main__":
    app.run(debug=True)

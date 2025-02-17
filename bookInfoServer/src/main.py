import base64
from flask import Flask, request, jsonify
from PIL import Image
import io
from integration import getBookTitles

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def foo(picture):
    # Placeholder for the actual implementation of foo
    return f"bar"


@app.route("/upload", methods=["POST"])
def upload_picture():
    if not request.data:
        return jsonify({"error": "No data provided"}), 400

    print(f"Request Content-Type: {request.content_type}")  # Debugging
    # print(f"Request Data: {request.data}")  # Debugging
    # incoming request with base 64 image.
    data = request.get_json(force=True)
    if "picture" not in data:
        return jsonify({"error": "No image field in request"}), 400

    # Decode the Base64 string
    image_data = base64.b64decode(data["picture"])

    # Convert to an image
    image = Image.open(io.BytesIO(image_data))

    # this is an array.
    result = getBookTitles(image)

    return result


if __name__ == "__main__":
    app.run(debug=True)

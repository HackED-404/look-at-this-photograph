import base64
import io
import logging
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
from integration import getBookTitles
from PIL import Image

app = Flask(__name__)
CORS(
    app,
    resources={
        r"/upload": {"origins": "http://localhost:3000", "methods": ["POST", "OPTIONS"]}
    },
)


@app.route("/upload", methods=["POST"])
@cross_origin(origins="http://localhost:3000")
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
    app.run(port=8008, debug=True)

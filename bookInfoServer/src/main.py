import base64
import io
import logging
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
from integration import getBookTitles
from PIL import Image, UnidentifiedImageError
from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",  # <-- Solution
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

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
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file_data = request.files["file"]
    if not file_data:
        return jsonify({"error": "No selected file"}), 400
    if file_data.content_type not in ["image/jpeg", "image/png", "image/gif"]:
        return "Invalid file type", 400

    # Decode the base64-encoded image data
    logging.info(f"Type of file_data: {type(file_data)}")
    logging.info(f"File data: {file_data}")
    file_data.seek(0)
    image_stream = io.BytesIO(file_data.read())
    image = Image.open(image_stream)

    # Get book titles from image
    result = getBookTitles(image)

    return jsonify(result)


if __name__ == "__main__":
    app.run(port=8008, debug=True)

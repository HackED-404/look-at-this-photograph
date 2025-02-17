
# Intro

This is the Flask-based server for receiving RESTful requests for interacting
with our server to get information about books based on images.

# Install

1. You should have the whole reposotory cloned to your local machine.
2. You should have Python 3 installed on your machine.
3. Install tesseract-ocr on your machine. You can find the installation guide
   [here](https://tesseract-ocr.github.io/tessdoc/Installation.html).
3. Install the dependencies with the following command:
```bash
pip install -r requirements.txt
```
4. Set your current working directory to the `bookInfoServer` directory.
5. Install the editable dependencies with the following command:
```bash
pip install -e ../ocr ../bookInfo ../processImage ../integration
```
6. Start up server with the following command:
```bash
python main.py
```
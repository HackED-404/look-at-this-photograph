
# Intro

This is the Flask-based server for receiving RESTful requests for interacting
with our server to get information about books based on images.

# Install

1. You should have the whole reposotory cloned to your local machine.
2. You should have Python 3 installed on your machine.
3. Install tesseract-ocr on your machine. You can find the installation guide
   [here](https://tesseract-ocr.github.io/tessdoc/Installation.html).
4. Set the current working directory to the `bookInfoServer` directory.
5. Set up a Python virtual environment with the following command:
```bash
python -m venv venv
```
6. Activate the virtual environment with the following command:
```bash
# mac or linux
source venv/bin/activate
# windows
venv\Scripts\activate
```
7. Install the dependencies with the following command (you may need to check if setup.py has everything that requirements.txt has):
```bash
pip install .
```
8. Set your current working directory to the `bookInfoServer` directory.
9. Install the editable dependencies with the following command:
```bash
pip install -e ../ocr ../book_data ../process_image ../integration
# OR
pip install -e ../ocr -e ../book_data -e ../process_image -e ../integration
```
10. The book_data service fetches book information from the Google Books. It
   relies on an API key to do so. The team is storing the key locally and if
   you don't have it, you have to ask for it (or get your own). The program will
   detect the key as long as it is stored as follows:
```bash
# mac or linux
export LATP_API_KEY='your_api_key_here'
# windows
set LATP_API_KEY='your_api_key_here'
```
10. Start up server with the following command:
```bash
python main.py
```
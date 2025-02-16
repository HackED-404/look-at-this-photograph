from setuptools import setup, find_packages

setup(
    name="get_boxes",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "opencv-contrib-python",
        "opencv-python",
        "packaging",
        "pillow",
        "pytesseract",
    ],
)

from setuptools import setup, find_packages

setup(
    name="imageTextExtraction",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "packaging",
        "pillow",
        "pytesseract",
        "matplotlib",
        "pytest",
        "opencv-python",
        "numpy",
    ],
)

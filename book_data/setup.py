from setuptools import setup, find_packages

setup(
    name="get_book_data",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["requests", "urllib3", "python-dotenv"],
)

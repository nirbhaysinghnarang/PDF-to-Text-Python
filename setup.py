import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdf_to_txt-nirbhay.py", # Replace with your own username
    version="0.0.1",
    author="Nirbhay Narang",
    author_email="snirbhay799@gmail.com",
    description="A small package to extract text from a pdf and save it in a .txt file.",
    url="https://github.com/nirbhay-py/pdf_to_text/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

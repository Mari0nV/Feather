import setuptools


setuptools.setup(
    name="game",
    version="0.0.1",
    author="Mari0nV",
    description="A small text game",
    url="https://github.com/Mari0nV/TextGame",
    packages=["game"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    requirements=["autocorrect", "nltk"]
)
import setuptools


setuptools.setup(
    name="feather",
    version="0.0.1",
    author="Mari0nV",
    description="A text game where you can write anything you want to do",
    url="https://github.com/Mari0nV/Feather",
    packages=["feather"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "nltk==3.5",
        "autocorrect==2.1.0"
        ]
)
from setuptools import setup

# python setup.py sdist
# pip install ./dist/convo-0.1.0.tar.gz

setup(
    name="convo",
    version="0.1.0",
    py_modules=["convo"],
    entry_points={"console_scripts": ["convo=convo:main"]},
    install_requires=[
        'pygments',
        'openai',
        'prompt-toolkit',
    ],
)

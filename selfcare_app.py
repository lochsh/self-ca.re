#!/usr/bin/env python

from flask import Flask, render_template
from selfcare import selfcare

app = Flask(__name__)

@app.route('/')
def sc():
    x = selfcare()
    return x

if __name__ == '__main__':
    app.run()

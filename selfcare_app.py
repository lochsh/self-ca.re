from flask import Flask
from selfcare import selfcare

app = Flask(__name__)


@app.route('/selfcare')
def sc():
    return selfcare()

if __name__ == '__main__':
    app.run()

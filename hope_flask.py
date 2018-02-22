from flask import Flask
from hope import first

app = Flask(__name__)
@app.route("/")
def main():

    return first.os()

app.run(host='0.0.0.0', port=80)

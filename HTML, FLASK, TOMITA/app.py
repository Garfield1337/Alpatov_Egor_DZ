import codecs
import subprocess
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/extract', methods=["post"])
def extract():
    us_input = request.form['txt']
    with codecs.open('./input.txt', 'w', 'utf-8') as file_input:
        file_input.write(str(us_input))
    parsim = ['./tomitaparser', 'config.proto']
    subprocess.check_output(parsim)
    return render_template('pretty.html')


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def stronadomowa():
    return '<h1>Witamy w Docker & Flask - test</h2>'

@app.route('/strona')
def strona():
    return render_template('strona.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world!<h2>'

if __name__=='__main__':
    app.run()
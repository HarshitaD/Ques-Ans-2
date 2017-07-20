from flask import Flask
app_lulu = Flask(__name__)

@app_lulu.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app_lulu.run(port=5000)

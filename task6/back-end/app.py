from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from the back-end!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)

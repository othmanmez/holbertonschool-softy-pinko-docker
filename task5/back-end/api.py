from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permet d'éviter les problèmes de CORS

@app.route('/api/hello', methods=['GET'])
def hello():
    return {"message": "Hello from the back-end!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)

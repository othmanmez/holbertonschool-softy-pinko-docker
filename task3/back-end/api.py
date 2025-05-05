from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permet les requêtes CORS (Cross-Origin) pour autoriser le front-end à accéder à l'API

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'  # Ce message sera renvoyé au front-end

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)  # L'API écoute sur le port 5252

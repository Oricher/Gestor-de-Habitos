from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

# Inicializa o app Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inicializa extensões
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Importa e registra as rotas
def register_routes():
    from routes import api
    app.register_blueprint(api)

register_routes()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

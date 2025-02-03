from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/test', methods=['GET'])
def test_route():
    return "API funcionando!"

@api.route('/', methods=['GET'])
def home():
    return "Bem-vindo ao Gestor de hábitos!"
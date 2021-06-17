#import o flask no app
from flask import Flask

#criando oobjeto
app = Flask(__name__)

#definindo uma rota para o site - mapeando a página principal
@app.route('/')
def index():
    return "Flopes say: Hello World"

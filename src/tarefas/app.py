from models.database import init_db

from flask import Flask, render_template 

app = Flask(__name__)

with app.app_context():
    init_db('data/tarefas.sql')

@app.route('/test')
def test():
    return 'Servidor online!'

@app.route('/')
def home():
    return render_template('base.html', titulo='Minha lista')


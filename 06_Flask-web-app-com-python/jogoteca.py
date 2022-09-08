from sys import flags
from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Scorn', 'Terror', 'PC')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
jogo4 = Jogo('Stray', 'Adventure', 'PS5')
lista = [jogo1, jogo2, jogo3,jogo4]          

app = Flask(__name__)
app.secret_key = 'senhaMuitoSecreta'


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome'] 
    categoria = request.form['categoria'] 
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return redirect('/') 
    #render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'senha123' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' - logado com sucesso')
        return redirect('/')
    else:
        flash('Usuário não logado')
        return redirect('/login')

app.run(debug=True)
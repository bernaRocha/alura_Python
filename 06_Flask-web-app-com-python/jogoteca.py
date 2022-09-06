from flask import Flask, render_template, request, redirect

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

lista = ['Tetris', 'Scorn', 'Stray', 'Crash']
jogo1 = 'Scorn'            

app = Flask(__name__)

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

app.run(debug=True)
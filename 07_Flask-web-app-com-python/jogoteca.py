from flask import Flask, render_template, request

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Scorn', 'Terror', 'PC')
jogo4 = Jogo('Stray', 'Adventure', 'PC')
jogo5 = Jogo('Mortal Kombat', 'Gore', 'PS1')
    
lista_jogos = [jogo1, jogo2, jogo3, jogo4, jogo5]

app = Flask(__name__)

@app.route('/inicio')
def ola():
    
    
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos )

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')

@app.route('/criar')
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)

    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

app.run()
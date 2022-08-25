from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
    jogo3 = Jogo('Scorn', 'Terror', 'PC')
    jogo4 = Jogo('Stray', 'Adventure', 'PC')
    jogo5 = Jogo('Mortal Kombat', 'Gore', 'PS1')
    
    lista_jogos = [jogo1, jogo2, jogo3, jogo4, jogo5]
    
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos )

app.run()
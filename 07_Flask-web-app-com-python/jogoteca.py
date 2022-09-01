from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lista = ['Tetris', 'Scorn', 'Stray', 'Crash']
    jogo1 = 'Scorn'
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run(debug=True)
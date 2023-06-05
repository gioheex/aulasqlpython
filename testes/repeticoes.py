from flask import Flask, render_template
app = Flask(__name__)


@app.route('/contagem/')
def contagem():
    saida = ''
    for numero in range(0, 1001, 2):
        saida += f'{numero}.'
    return render_template('contagem.html', cont=saida)

app.run()
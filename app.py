from flask import Flask, request, render_template
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calcular():
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = datetime.datetime.strptime(
            request.form['data-nascimento'], '%Y-%m-%d').date()

        idade = calcular_idade(data_nascimento)
        dias_vida = calcular_dias_vida(data_nascimento)
        minutos_vida = calcular_minutos_vida(data_nascimento)

        return render_template('resultado.html', nome=nome, idade=idade, dias_vida=dias_vida, minutos_vida=minutos_vida)
    return render_template('index.html')


def calcular_idade(data_nascimento):
    data_atual = datetime.date.today()
    idade = data_atual.year - data_nascimento.year
    if data_atual.month < data_nascimento.month or (data_atual.month == data_nascimento.month and data_atual.day < data_nascimento.day):
        idade -= 1
    return idade


def calcular_dias_vida(data_nascimento):
    data_atual = datetime.datetime.now().date()
    dias_vida = (data_atual - data_nascimento).days
    return dias_vida


def calcular_minutos_vida(data_nascimento):
    data_atual = datetime.datetime.now()
    minutos_vida = (data_atual - datetime.datetime.combine(data_nascimento,
                    datetime.datetime.min.time())).total_seconds() // 60
    return minutos_vida


if __name__ == '__main__':
    app.run(debug=True)

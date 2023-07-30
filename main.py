from flask import Flask, render_template, request
import weather_api

app = Flask(__name__)
@app.route('/')
def home():
    condicao_display = 'hidden'
    local = 'Digite algum local'
    return render_template('index.html', condicao_display=condicao_display, local=local)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obter a variável enviada pelo usuário
        inputValueLocal = request.form.get('localInput')

        # executar a função no weather_api.py e retornar valores para as variáveis abaixo
        local, temperatura, descricao, descricao_imagem, condicao_display, diaOuNoite, umidade, vento, data_existente = weather_api.processar_variavel(inputValueLocal)

        # log
        print(f'nome:{local}, temp: {temperatura}, desc:{descricao}, descricao_imagem:{descricao_imagem}, display:{condicao_display}, diaOuNoite:{diaOuNoite}, umidade:{umidade} vento:{vento}')

        # enviar os valores ao index.html
        return render_template('index.html', local=local, temperatura=temperatura, descricao=descricao, descricao_imagem=descricao_imagem, condicao_display=condicao_display, diaOuNoite=diaOuNoite, umidade=umidade, vento=vento, data_existente=data_existente)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)  # Run app

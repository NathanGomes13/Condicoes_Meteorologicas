import requests
import time
from pprint import pprint

# backup para manter variáveis anteriores em caso de erro
ultima_descricao = None
ultima_temperatura = None
ultima_local = None
ultima_descricao_imagem = None
ultima_diaOuNoite = None
ultima_umidade = None
ultima_vento = None

API_Key = 'f86060d9d723f8dd8519ccce7843a59d'

def processar_variavel(inputValueLocal):
    global ultima_descricao, ultima_temperatura, ultima_local, ultima_descricao_imagem, ultima_diaOuNoite, ultima_umidade, ultima_vento

    # confirmação de variável recebida
    print("Variável recebida:", inputValueLocal)
    local = inputValueLocal

    # requisição e formatação para json
    link_weather = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&lang=pt_br"+"&q="+local+"&units=metric"
    requisicao_weather = requests.get(link_weather).json()

    # unixtimestamp
    current_time = time.time()

    # prevenção de local não existente
    if requisicao_weather['cod'] == '400' or requisicao_weather['cod'] == '404':
        data_existente = 'Local inválido'

        # manter antigos dados
        if ultima_descricao is not None:
            descricao = ultima_descricao
            condicao_display = 'visible'
        else:
            descricao = ''
            condicao_display = 'hidden'

        if ultima_temperatura is not None:
            temperatura = ultima_temperatura
            condicao_display = 'visible'
        else:
            temperatura = ''
            condicao_display = 'hidden'

        if ultima_local is not None:
            local = ultima_local
            condicao_display = 'visible'
        else:
            local = 'Digite algum local'
            condicao_display = 'hidden'

        if ultima_descricao_imagem is not None:
            descricao_imagem = ultima_descricao_imagem
            condicao_display = 'visible'
        else:
            descricao_imagem = ''
            condicao_display = 'hidden'

        if ultima_diaOuNoite is not None:
            diaOuNoite = ultima_diaOuNoite
            condicao_display = 'visible'
        else:
            diaOuNoite = ''
            condicao_display = 'hidden'

        if ultima_umidade is not None:
            umidade = ultima_umidade
            condicao_display = 'visible'
        else:
            umidade = ''
            condicao_display = 'hidden'

        if ultima_vento is not None:
            vento = ultima_vento
            condicao_display = 'visible'
        else:
            vento = ''
            condicao_display = 'hidden'

        return local, temperatura, descricao, descricao_imagem, condicao_display, diaOuNoite, umidade, vento, data_existente
    else:
        condicao_display = "visible"
        descricao = requisicao_weather['weather'][0]['description']
        temperatura_data = requisicao_weather['main']['temp']
        temperatura = f'{temperatura_data:,.0f}º'
        local = requisicao_weather['name']
        descricao_imagem = requisicao_weather['weather'][0]['main']
        umidade_data = requisicao_weather['main']['humidity']
        umidade = f'{umidade_data}%'
        vento_data = requisicao_weather['wind']['speed']
        vento = f'{temperatura_data} km/h'
        sunrise = requisicao_weather["sys"]["sunrise"]
        sunset = requisicao_weather["sys"]["sunset"]
        data_existente = ''

        # se está de dia ou de noite
        if sunrise < current_time < sunset:
            diaOuNoite = 'Dia'
        else:
            diaOuNoite = 'Noite'
        pprint(requisicao_weather)

        # atualizar as variáveis globais com os novos valores
        ultima_descricao = descricao
        ultima_temperatura = temperatura
        ultima_local = local
        ultima_descricao_imagem = descricao_imagem
        ultima_diaOuNoite = diaOuNoite
        ultima_umidade = umidade
        ultima_vento = vento


        # Retornar as variáveis ao main.py
        return local, temperatura, descricao, descricao_imagem, condicao_display, diaOuNoite, umidade, vento, data_existente
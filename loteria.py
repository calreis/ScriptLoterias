import pandas as pd, requests

''' Este script foi criado para um amigo verificar os últimos resultados da loteria de acordo
    com necessidade de n resultados'''

# função criada para deixar o código mais limpo e organizado.
# Pretendo modularizá-lo para organizar melhor o código

def lot():
    # Variável que lê o númnero do concurso que deseja verificar.
    concurso = int(input('Digite o número do concurso que deseja verificar: '))
    # Contador para retornar uma nova requisição na API
    c = 0
    # As requisições são feitas na API https://loteriascaixa-api.herokuapp.com/swagger-ui/
    url = f'https://loteriascaixa-api.herokuapp.com/api/megasena/{concurso}'
    response = requests.get(url)
    dados = response.json() # o retorno é feito em Json pela arquiterura do arquivo.
    
    num = dados['dezenas'] # chave do dicionário dados que consta a lista de dezenas
    lista = [] # lista vázia para adicionar as dezenas com o função append.

    while c < 200: # O contador inicia em zero, enquanto for menor que zero sera feita a requisição.
        lista.append(num)
        concurso-=1
        url = f'https://loteriascaixa-api.herokuapp.com/api/megasena/{concurso}'
        response = requests.get(url)
        dados = response.json() # é uma redundância eu sei rsrsrsrs
        num = dados['dezenas']
        c+=1
    
    for dezenas in lista:
        S_dezenas = pd.Series(lista)
    
    return S_dezenas

den = lot()
print(den)
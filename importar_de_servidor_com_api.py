import requests

def enviar_arquivo():
    local = 'C:/Users/Regina/Downloads/Teste.xlsx'
    requisicao = requests.post('https://upload.gofile.io/uploadFile', files={'file': open(local, 'rb')})
    saida_requisicao = requisicao.json()
    print(saida_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print("Arquivo enviado", url)

def receber_arquivo(file_url):
    requisicao = requests.get(file_url)
    if requisicao.ok:
        with open('arquivo baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print("Arquivo baixado")
    else:
        print("Erro ao baixar", requisicao.json())

def enviar_arquivo_chave():
    caminho = 'C:/Users/Regina/Downloads/teste.xlsx'
    chave_acesso = 'F51foI5qgwxvNqPZZxXvC9Cu12dlpyS0'
    requisicao = requests.post(
        url='https://upload.gofile.io/uploadFile',
        files={'file': open(caminho, 'rb')},
        data={'token': chave_acesso}
    )
    saida_requisicao = requisicao.json()
    print(saida_requisicao)
#enviar_arquivo()

#enviar_arquivo()
enviar_arquivo_chave()
#receber_arquivo('https://gofile.io/d/6M4dZZ') aqui entra o link gerado no arquivo enviado,mas primeiro precisa executar enviar arquivo

import requests

def enviar_arquivo():
    local = 'C:/Users/Regina/Downloads/teste.xlsx'
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
    chave_acesso = '123'
    requisicao = requests.post(
        url='https://file.io',
        files={'file': open(caminho, 'rb')},
        headers={'Authorization': chave_acesso}
    )
    saida_requisicao = requisicao.json()
    print(saida_requisicao)


enviar_arquivo()
enviar_arquivo_chave()
#receber_arquivo('https://gofile.io/d/DJOp5A')

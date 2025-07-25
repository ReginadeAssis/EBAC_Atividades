def enviar_com_bearer():
    import requests

    caminho = 'C:/Users/Regina/Downloads/teste.xlsx'
    chave_acesso = 'F51foI5qgwxvNqPZZxXvC9Cu12dlpyS0'
    headers = {'Authorization': f'Bearer {chave_acesso}'}

    requisicao = requests.post(
        url='https://upload.gofile.io/uploadfile',
        files={'file': open(caminho, 'rb')},
        headers=headers
    )

	print(requisicao.json())


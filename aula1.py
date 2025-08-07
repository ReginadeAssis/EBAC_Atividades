import requests

response = requests.get('https://finance.yahoo.com/quote/PETR4.SA/history/')

print(response.text[0:9])

#primeiro teste

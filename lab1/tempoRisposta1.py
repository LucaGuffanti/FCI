import requests

#r diventa l'oggetto della get request
r = requests.get('http://google.com')

print('Tempo necessario:')
print(r.elapsed.microseconds/1000, 'ms')


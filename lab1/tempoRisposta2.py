import requests

ripetizioni = int(input('Inserire il numero di tentativi: '))
misurazioni = []

# inseriamo la richiesta precedente in un ciclo for
for x in range(ripetizioni):
    r = requests.get('http://google.com')
    tempo = r.elapsed.microseconds / 1000
    misurazioni.append(tempo)
    print(tempo)

print('\n\n')
print('tempo minimo:', min(misurazioni))
print('tempo massimo:', max(misurazioni))
print('tempo medio: ', sum(misurazioni)/len(misurazioni))

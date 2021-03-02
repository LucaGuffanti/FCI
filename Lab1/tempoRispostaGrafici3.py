#si vuole stampare un grafico per sito
from matplotlib import markers
import requests
import matplotlib.pyplot as plt

siti = ['http://www.polimi.it', 'http://youtube.com', 'http://facebook.com']


massimo = 0
i = 1


for site in siti:
    tempi = []
    for x in range(10):
        r = requests.get(site)
        tempi.append(r.elapsed.microseconds/1000)

    massimo = max(massimo, max(tempi))

    plt.subplot(1,len(siti),i)
    plt.plot(tempi)
    plt.title("Tempo")
#    plt.figure(i)
#    plt.plot(tempi, label=site)
#    plt.title("Tempo")

    
    i = i + 1

plt.show()    
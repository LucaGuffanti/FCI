from matplotlib import markers
import requests
import matplotlib.pyplot as plt

siti = ['http://www.polimi.it', 'http://youtube.com', 'http://facebook.com']

plt.figure()

massimo = 0

for site in siti:
    tempi = []
    for x in range(10):
        r = requests.get(site)
        tempi.append(r.elapsed.microseconds/1000)

    massimo = max(massimo, max(tempi))
    plt.plot(tempi, label=site)
    print("Sito", site)
    print("Tempo Minimo: ", min(tempi))
    print("Tempo Massimo: ", max(tempi))


print("Massimo Assoluto: ", massimo)
plt.ylim(0, massimo*1.1)
plt.title("Tempi di Download Homepage")
plt.xlabel("ID")
plt.ylabel("Tempi (ms)")
plt.legend(loc='lower right', fontsize=10)
plt.show()
    
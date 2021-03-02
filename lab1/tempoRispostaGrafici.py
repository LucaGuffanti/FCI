import requests
import matplotlib.pyplot as plt


tempi = []
for i in range(20):
    r = requests.get("http://google.com")
    tempi.append(r.elapsed.microseconds/1000)

plt.figure()
plt.title('MISURAZIONI DEI RITARDI')
plt.xlabel('ID RICHIESTA')
plt.ylabel('TEMPO')
plt.ylim([0.9*min(tempi), 1.1*max(tempi)])
plt.grid()
plt.plot(tempi)
plt.show()

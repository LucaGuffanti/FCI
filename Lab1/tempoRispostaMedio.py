import requests

urls = ['http://google.com', 'http://youtube.com']
bestAvg = 0
avg = 0
defined = False
tempo = []

for url in urls:
    for x in range(10):
        r = requests.get(url) 
        tempo.append(r.elapsed.microseconds/1000)
    avg = sum(tempo)/len(tempo)
    if defined == False:
        bestAvg = avg 
        defined = True  
    else:
        bestAvg = min(bestAvg, avg)

print("Tempo medio migliore:", bestAvg)
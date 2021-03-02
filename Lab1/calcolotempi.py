import requests

def best_avg(lista: list, num: int):
    
    best = 0
    ndef = True
    avg = 0
    tempi = []

    for url in lista:
        for x in range(num):
            r = requests.get(url)
            tempi.append(r.elapsed.microseconds/1000)
        avg = sum(tempi)/len(tempi)
        if ndef == True:
            best = avg
            ndef = False
        else:
            best = min(avg, best)

    return best


if __name__ == "__main__":
    lista = [
            'http://www.google.com', 
            'http://www.youtube.com', 
            'http://www.polimi.it', 
            'http://www.wikipedia.org', 
            'http://www.amazon.com',
            'http://www.twitter.com'
            ]

    num = 5

    print(best_avg(lista, num))
from socket import *

def isPrime(n : int):
    i = 2
    prime = True

    while i*i <= n and prime is True:
        if n%i == 0:
            prime = False
        i += 1

    return 'Primo' if prime else 'Non Primo'

if __name__ == '__main__':
    
    serverPort = 13000
    mDimension = 2048

    # creazione della socket e binding del numero di porta
    
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    print(f'Server in ascolto sulla porta {serverPort}')

    # ricezione del messaggio
    while True:
        message, clientAddress = serverSocket.recvfrom(mDimension)

        # decoding del messaggio e valutazione della richiesta

        decodedMessage = message.decode('utf-8')
        print(f'Ricevuto {decodedMessage} da {clientAddress}')

        number = int(decodedMessage)
        message = isPrime(number)

        # invio del messaggio al client

        serverSocket.sendto(message.encode('utf-8'), clientAddress)
        
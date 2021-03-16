from socket import *

serverPort = 12000

# apriamo la socket per il server

serverSocket = socket(AF_INET, SOCK_DGRAM)

# ora bisogna associare il numero di porta alla socket
# tramite l'operazione bind
# in questo modo il processo server utilizzarà la specifica
# porta che gli abbiamo associato

serverSocket.bind(('', serverPort))

print('Server pronto per la comunicazione.')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode('utf-8')
    print(f'Messaggio Ricevuto da: {clientAddress}')
    print(f'Oggetto del Messaggio: {message}')

    modifiedMessage = message.upper()

    # ora il server è pronto a rispondere al client
    serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)
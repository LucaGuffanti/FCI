from socket import *

# numero di porta usata per il welcome socket
serverPort = 12000

# apriamo ora la Welcome Socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# forziamo l'associazione tra la socket aperta e il numero
# di porta che abbiamo deciso
serverSocket.bind(('', serverPort))

# mettiamo il welcome socket in ascolto delle richieste
# di connessione da altri client TCP
# l'intero specifica la lunghezza della coda delle
# connessioni non ancora accettate
serverSocket.listen(1)

print('Server in ascolto. Pronto a ricevere')
while True:
    # attendiamo le richieste di connessione da altri client
    # con una richiesta che viene accettata, viene creata un nuova
    # connection socket, e vengono anche ritornate le generalità del
    # client tcp
    connectionSocket, clientAddress = serverSocket.accept()
    print('Connesso con', clientAddress)

    message = connectionSocket.recv(1024)
    message = message.decode('utf-8')
    modifiedMessage = message.upper()

    connectionSocket.send(modifiedMessage.encode('utf-8'))
    connectionSocket.close()
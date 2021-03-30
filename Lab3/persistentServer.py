# vogliamo terminare la connessione nell'invio di un punto

from socket import *

serverPort = 12000


serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen()

print('Server in ascolto. Pronto a ricevere')
while True:

    connectionSocket, clientAddress = serverSocket.accept()
    print('Connesso con', clientAddress)
    while True:
        message = connectionSocket.recv(1024)
        message = message.decode('utf-8')
        if message == '.':
            break
        modifiedMessage = message.upper()

        connectionSocket.send(modifiedMessage.encode('utf-8'))
    
    connectionSocket.close()
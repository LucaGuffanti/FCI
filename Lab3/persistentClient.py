# vogliamo terminare la connessione nell'invio di un punto
# applicazione client persistente tcp

from socket import *

# identifico il welcome socket del server, come coppia di IP e Porta
serverName = '192.168.1.3'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)


clientSocket.connect((serverName, serverPort))

while True:
    message = input('Inserire una frase (. per fermare):')
    
    clientSocket.send(message.encode('utf-8'))
    
    if message == '.':
        break

    modifiedMessage = clientSocket.recv(1024)
    modifiedMessage = modifiedMessage.decode('utf-8')

    print(modifiedMessage)


clientSocket.close()
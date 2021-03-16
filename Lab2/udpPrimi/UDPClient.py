from socket import *

serverName = 'localhost'
serverPort = 13000
mDimension = 2048
sTimeout = 5

serverAddress = (serverName, serverPort)

# apertura della socket, predisposizione del timeout e input

clientSocket = socket(AF_INET, SOCK_DGRAM) 
clientSocket.settimeout(sTimeout)
message = input('Inserire un numero: ')

# invio del messaggio

clientSocket.sendto(message.encode('utf-8'), serverAddress)

# ricezione del messaggio di risposta nel costrutto per verifica
# di errore

try:
    message, serverAddress = clientSocket.recvfrom(mDimension)
    decodedMessage = message.decode('utf-8')
    print(f'Message \"{decodedMessage}\" from {serverAddress}')
except:
    print('Timeout error: server non raggiungibile')
finally:
    # chiusura della socket
    clientSocket.close()
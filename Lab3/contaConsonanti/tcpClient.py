from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(5)

clientSocket.connect((serverName, serverPort))

stringa = input('Inserire una stringa:')
clientSocket.send(stringa.encode('utf-8'))

risultato = clientSocket.recv(1024)

risultato = risultato.decode('utf-8')
print(risultato)
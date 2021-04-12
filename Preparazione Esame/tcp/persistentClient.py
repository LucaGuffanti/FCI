from socket import *

# identifico la welcome socket del server
serverName = 'localhost'
serverPort = 15000

# creo la socket client, SOCK_STREAM per TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# imposto il timeout
clientSocket.settimeout(5)

# apro una connessione con il server 
clientSocket.connect((serverName, serverPort))

while True:
    message = input('inserire una stringa (.) per terminare la connessione: ')
   
    clientSocket.send(message.encode('utf-8'))
    if message == '.':
            break
    received = clientSocket.recv(2048)
    received = received.decode('utf-8')
    print(received)


clientSocket.close()


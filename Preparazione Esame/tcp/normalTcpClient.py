from socket import *

# identifico la welcome socket del server
serverName = 'localhost'
serverPort = 15000

# creo la socket, non è necessario eseguire il binding
clientSocket = socket(AF_INET, SOCK_STREAM)

# apro una connessione
clientSocket.connect((serverName, serverPort))

# richiedo un numero 
num = input('Inserire un numero: ')

clientSocket.send(num.encode('utf-8'))

response = clientSocket.recv(2048)
response = response.decode('utf-8')

print(response)

clientSocket.close()
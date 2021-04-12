from socket import *

#definisco la welcome socket, tramite il numero di porta
serverPort = 15000

welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket.bind(('', serverPort))

welcomeSocket.listen()
print('server listening...')
while True:
   
    connSocket, clientAddress = welcomeSocket.accept()
    while True:
        message = connSocket.recv(2048)
        message = message.decode('utf-8')
        print(f'message {message} from {clientAddress}')
        if(message == '.'):
            break
        result = message[::-1]
        connSocket.send(result.encode('utf-8'))

    connSocket.close()

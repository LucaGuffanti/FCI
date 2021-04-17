from socket import *

serverPort = 15000

welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket.bind(('', serverPort))

welcomeSocket.listen()
while True:
    serverSocket, clientAddress = welcomeSocket.accept()
    message = serverSocket.recv(2048)

    message = message.decode('utf-8')
    result = ''
    for i in range(0, int(message) + 1):
        result = result + str(i) +', '
    serverSocket.send(result.encode('utf-8'))

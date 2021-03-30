from socket import *

def countConsonant(message: str):
    cons = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in message:
        if letter not in vowels:
            cons += 1
    return cons


serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print('Listening')

while True:
    connectionSocket, clientAddress = serverSocket.accept()
    message = connectionSocket.recv(1024)
    message = message.decode('utf-8')

    result = countConsonant(message)
    messageToSend = '# di consonanti' + str(result)
    connectionSocket.send(messageToSend.encode('utf-8'))

    connectionSocket.close
from socket import *

serverName = 'localhost'
serverPort = 12001

tempo = 5

serverAddress = (serverName, serverPort)

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(tempo)

message = input('Inserire un messaggio: ')

clientSocket.sendto(message.encode('utf-8'), serverAddress)

try:
    encoded, serverAddress = clientSocket.recvfrom(2048)
    realMessage = encoded.decode('utf-8')
    print(realMessage)
except:
    print('Server non raggiungibile: Timeout Error')
finally:
    clientSocket.close()
from socket import *

# identifico il server
serverPort = 13000

# creo la socket ed eseguo il bind
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print('server ready...')

while True:
    # attendo un messaggio
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode('utf-8')
    print(f'message {message} from {clientAddress}')

    # elaboro il messaggio ricevuto
    result = message[::-1]
    serverSocket.sendto(result.encode('utf-8'), clientAddress)

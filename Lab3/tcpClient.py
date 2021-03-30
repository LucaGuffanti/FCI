# applicazione client tcp

from socket import *

# identifico il welcome socket del server, come coppia di IP e Porta
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(5)

# si richiede di aprire una connessione con il server
# specificando l'indizzo del welcome socket del server
clientSocket.connect((serverName, serverPort))

# dopo che il server ha accettato la connessione
# ed è avvenuto il setup della connessione stessa
# si può continuare

message = input('Inserire una frase:')

# non abbiamo specificato l'indirizzo a cui inviare il
# messaggio, ma i due host si sono scambiati le generalità
# dei CONNECTION SOCKET, quindi sappiamo già l'indirizzo
clientSocket.send(message.encode('utf-8'))

# attendiamo ora i messaggi dal server
modifiedMessage = clientSocket.recv(1024)
modifiedMessage = modifiedMessage.decode('utf-8')

print('Messaggio: ', modifiedMessage)

clientSocket.close()
from socket import *

# identifico il server tramite numero di porta e indirizzo ip
serverName = 'localhost'
serverPort = 13000

t_out = 5

# creo la socket UDP, utilizzando i datagrammi
clientSocket = socket(AF_INET, SOCK_DGRAM)

#clientSocket.bind(('', 45000))

# non devo eseguire l'operazione di bind per la socket UDP

# utilizziamo un timeout, lato client
clientSocket.settimeout(t_out)

# creo un messaggio, immaginiamo che il server ritorni la stringa inviata al contrario
message = input('inserire una stringa')

# invio ora il messaggio
clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))

# attendo una risposta, implementando la verifica di un errore
try:
    received, serverAddress = clientSocket.recvfrom(2048)
    received = received.decode('utf-8')
    print(message, received)
except:
    print('Errore da lato server')
finally:
    clientSocket.close()

from socket import *
# definisco i dati per la socket cioè l'indirizzo IP e la Porta

serverName = 'localhost'  # 127.0.0.1
serverPort = 12001  # arbitrario tranne quelli standardizzati

# costruisco la socket
# AF_INET si riferisce al tipo di indirizzo IP
# SOCK_DGRAM si riferisce all'udilizzo di UDP

clientSocket = socket(AF_INET, SOCK_DGRAM)

tm = 10

clientSocket.settimeout(tm)

# richiesta stringa all'utente

message = input('Inserisci una Stringa: ')

# usiamo la socket appena creata per comunicare con il server
# usiamo il messaggio in binario e identifichiamo il destinatario come una tupla

clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))



# troviamo una soluzione per l'attesa infinita della risposta:
# possiamo impostare un timeout e generare un'exception


# attendiamo ora la ricezione del messaggio
# la funzione ritorna sia i dati che le generalità del mittente
# prende come argomento la lunghezza del buffer in entrata (in BYTE)
try:
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    # decodifichiamo dal binario e stampiamo il messaggio

    modifiedMessage = modifiedMessage.decode('utf-8')
    print(f'Messaggio ricevuto da: {serverAddress}')
    print(modifiedMessage)
except:
    print('Timeout Scaduto: Server non raggiungibile')
finally:
    # chiudiamo la socket       

    clientSocket.close()

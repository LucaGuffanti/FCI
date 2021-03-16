# info
    laboratorio su programmazione di socket
    per scambi tra client e server di tipo PULL
# teoria
    nel laboratorio di oggi programmiamo, sfruttando SOCKET API di python un server UDP e un client UDP.
    nella comunicazione tra client è server, è necessario che il server sia avviato prima della ricezione, e il client, anch'esso dotato di socket, dovrà conoscere l'indirizzo ip del server e il numero di porta del processo applicativo. la stessa cosa vale per il server, dato che deve essere in grado di comunicare con il client.

    la caratteristica di udp è l'offerta di un trasporto di tipo connectionless, senza l'implementazione di tecniche per il recupero di dati persi durante la comunicazione -> comunicazione meno affidabile rispetto a TCP.
    
    
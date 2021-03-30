# info
    Programmazione di socket TCP in python
# teoria
    Il servizio di trasporto TCP è un protocollo
    che garantisce l'instaurazione di un trasporto affidabile.
    Il socket nella comunicazione è presente sia nel client che nel server: 
    dovrà essere aperta una porta verso la rete per poter comunicare. 
    Il processo di comunicazione, soprattutto nel lato del server, è diverso rispetto a UDP.

    il server dovrà aprire un socket, che dovrà essere già aperto.
    il socket viene definito "Welcome Socket": assomiglia al socket UDP ed è in grado di ricevere da tutti i client,
    con i client che per connettersi dovranno specificare l'indirizzo del welcome socket.
    
    Nel momento del contatto tra i due host, viene richiesta l'apertura di una connessione.
    Aperta la connessione inizia la trasmissione. Quando contattato dal client il server crea un nuovo socket (Connection Socket) diverso dal Welcome
    Socket, per gestire privatamente la connessione tra client e server. in questo modo il server è in grado di monitorare i parametri
    di stato della connessione e implementare processi per preservare le informazioni scambiate, garantendo l'affidabilità.



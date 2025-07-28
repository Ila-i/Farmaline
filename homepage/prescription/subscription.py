class TesseraSanitaria :
    codice_fiscale: str
    sesso: str
    luogo_nascita: str
    provincia: str
    data_nascita: str
    data_scadenza: str
    numero_identificazione_tessera: str

    def __init__(self):
        self.codice_fiscale = input(" CODICE FISCALE : ")
        self.sesso = input(" SESSO : ")
        self.luogo_nascita = input(" LUOGO DI NASCITA : ")
        self.provincia = input(" PROVINCIA : ")
        self.data_nascita = input(" DATA DI NASCITA : ")
        self.data_scadenza = input(" DATA DI SCADENZA : ")
        self.numero_identificazione_tessera = input(" NUMERO IDENTIFICAZIONE TESSERA : ")

class Cliente :
    t_s: TesseraSanitaria #t_s abbreviazione tessera sanitaria
    nome:str
    cognome:str

    def __init__(self):
        self.nome= input("Inserire il proprio nome : ")
        self.cognome = input("Inserire il proprio cognome : ")
        self.t_s.__init__()

class ProfiloUtente :
    nome_utente:str
    password: str
    utente: Cliente

    def __init__(self,cliente : Cliente):
        utente = cliente
        nome_utente = input(" inserire un nome utente : ") # inserire controllo per corrispondenza profilo utente
        password = input(" inserire una password : ")



def registrarsi (lista_clienti: Cliente) -> ProfiloUtente :
    cliente: Cliente
    profilo : ProfiloUtente
    print( "per registrarsi inserire i dati richiesti : ")
    cliente.__init__()

    #controllo esistenza cliente nel database
    for i in range(len(lista_clienti)) :
        if cliente == lista_clienti[i] :
            print(" utente già registrato ")
            break
        else :
            lista_clienti.append(cliente)
            print(" registrazione effettuata con successo : ")
            #creazione profilo utente
            profilo.__init__(cliente)
            return profilo





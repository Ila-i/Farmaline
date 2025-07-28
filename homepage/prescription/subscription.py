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
        self.t_s = TesseraSanitaria()

class ProfiloUtente :
    nome_utente:str
    password: str
    utente: Cliente

    def __init__(self,cliente : Cliente):
        self.utente = cliente
        self.nome_utente = input(" inserire un nome utente : ") # inserire controllo per corrispondenza profilo utente
        self.password = input(" inserire una password : ")



def registrarsi (lista_clienti : list[Cliente]) -> ProfiloUtente :
    cliente = Cliente()
    print( "per registrarsi inserire i dati richiesti : ")
    #controllo esistenza cliente nel database
    for i in range(len(lista_clienti)) :
        if cliente.t_s.codice_fiscale == lista_clienti[i].t_s.codice_fiscale:
            print(" utente già registrato ")
            break

    lista_clienti.append(cliente)
    # creazione profilo utente
    profilo= ProfiloUtente(cliente)
    print(f"""  registrazione effettuata con successo 
    Benvenuto {profilo.nome_utente} !""")
    return profilo





print("inizializzazione lista ")
lista = []
controllo = "go"
while controllo != "exit" :
    print("inizio registrazione")
    profilo = registrarsi(lista)
    controllo = input("controllo")




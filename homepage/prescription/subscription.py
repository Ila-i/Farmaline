class TesseraSanitaria :
    codice_fiscale: str
    sesso: str
    luogo_nascita: str
    provincia: str
    data_nascita: str
    data_scadenza: str
    numero_identificazione_tessera: str

    def controllo(self, messaggio: str, lunghezza: int) -> str : #controllo del numero dei caratteri alfanumerici( va aggiunto se si riesce il controllo più specifico o messo come eccezione
       parametro = input(messaggio)
       while len(parametro) != lunghezza :
            parametro = input(f" il parametro non è valido, riprovare : ")

       return parametro

    def __init__(self):
        print( " Di seguito si inseriscano i dati della tessera sanitaria : ")
        self.codice_fiscale = self.controllo(" CODICE FISCALE :", 16) # nel codice fiscale si contano 16 caratteri alfanumerici
        self.sesso = self.controllo(" SESSO : ", 1)
        self.luogo_nascita = input(" LUOGO DI NASCITA : ")
        self.provincia = self.controllo(" PROVINCIA : ", 2)
        self.data_nascita = self.controllo(" DATA DI NASCITA (gg/mm/aaaa) : ", 10)
        self.data_scadenza = self.controllo(" DATA DI SCADENZA (gg/mm/aaaa) : ", 10)
        self.numero_identificazione_tessera = self.controllo(" NUMERO IDENTIFICAZIONE TESSERA SANITARIA : ", 20)# sulla tessera sanitaria fisica sono 20 caratteri alfanumerici


class Cliente :
    t_s: TesseraSanitaria #t_s abbreviazione tessera sanitaria
    nome:str
    cognome:str

    def __init__(self):
        self.nome= input("Inserire il proprio nome : ")
        self.cognome = input("Inserire il proprio cognome : ")
        self.t_s = TesseraSanitaria()
    #def ricerca ()# da database per controllo su presenza o meno della persona

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




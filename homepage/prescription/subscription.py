class TesseraSanitaria :
    codice_fiscale: str
    sesso: str
    luogo_nascita: str
    provincia: str
    data_nascita: str
    data_scadenza: str
    numero_identificazione_tessera: str

    def controllo(self, parametro: str, lunghezza: int) -> str :
       parametro = input()

       while len(parametro) != lunghezza :
            print(f" il parametro non è valido, riprovare")
            parametro = input()

       return parametro

    def __init__(self):
        print(" CODICE FISCALE : ")
        self.codice_fiscale =self.controllo(self.codice_fiscale, 16) # nel codice fiscale si contano 16 caratteri alfanumerici
        print(" SESSO : ")
        self.sesso = self.controllo(self.sesso, 1)
        self.luogo_nascita = input(" LUOGO DI NASCITA : ")
        print(" PROVINCIA : ")
        self.provincia = self.controllo(self.provincia, 2)
        print(" DATA DI NASCITA (gg/mm/aaaa) : ")
        self.data_nascita = self.controllo(self.data_nascita, 10)
        print(" DATA DI SCADENZA (gg/mm/aaaa) : ")
        self.data_scadenza = self.controllo(self.data_scadenza, 10)
        input(" NUMERO IDENTIFICAZIONE TESSERA : ")
        self.numero_identificazione_tessera = self.controllo(self.numero_identificazione_tessera, 20)# sulla tessera fisica sono 20 caratteri alfanumerici


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




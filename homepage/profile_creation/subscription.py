from abc import ABC, abstractmethod
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#engine = create_engine('postgresql:/postgres@PostgreSQL17/Farmaline')
engine = create_engine('postgresql+psycopg2://postgresql:postgres@localhost:5432/Farmaline')

session = sessionmaker(bind=engine)

class Persona (ABC) :
    nome: str
    cognome: str

    def __init__(self):
        self.nome = input("Inserire il proprio nome : ")
        self.cognome = input("Inserire il proprio cognome : ")

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

#TODO quando possibile inserire controllo data di nascita e scadenza tessera sanitaria

    def __init__(self):
        print( " Di seguito si inseriscano i dati della tessera sanitaria : ")
        self.codice_fiscale = self.controllo(" CODICE FISCALE :", 16) # nel codice fiscale si contano 16 caratteri alfanumerici
        self.sesso = self.controllo(" SESSO : ", 1)
        self.luogo_nascita = input(" LUOGO DI NASCITA : ")
        self.provincia = self.controllo(" PROVINCIA : ", 2)
        self.data_nascita = self.controllo(" DATA DI NASCITA (gg/mm/aaaa) : ", 10)
        self.data_scadenza = self.controllo(" DATA DI SCADENZA (gg/mm/aaaa) : ", 10)
        self.numero_identificazione_tessera = self.controllo(" NUMERO IDENTIFICAZIONE TESSERA : ", 20)# sulla tessera sanitaria fisica sono 20 caratteri alfanumerici

class Cliente(Persona):
    t_s: TesseraSanitaria #t_s abbreviazione tessera sanitaria

    def __init__(self):
        super().__init__()
        self.t_s = TesseraSanitaria()
    #def ricerca () # da database per controllo su presenza o meno della persona

class TesserinoProfessionale :
    ordine_di_appartenenza: str # indica il settore lavorativo a cui appartieni
    n_matricola : str # indica il numero di iscrizione all'albo di riferimento

    def __init__(self, ordine :str):
        self.ordine_di_appartenenza = ordine
        self.n_iscrizione_albo = input("Inserire il proprio numero di matricola : ")

class Farmacista(Persona):
    t_p: TesserinoProfessionale #t_p abbreviazione tesserino professionale

    def __init__(self):
        super().__init__()
        self.t_p = TesserinoProfessionale("farmacista")
    #def ricerca () # da database per controllo su presenza o meno della persona

class ProfiloUtente :
    nome_utente:str
    password: str
    utente: Persona

    def __init__(self,user : Persona):
        self.utente = user
        self.nome_utente = input(" inserire un nome utente : ") # inserire controllo per corrispondenza profilo utente
        self.password = input(" inserire una password : ")



def registrarsi (user : str) -> ProfiloUtente :

    if user == "Cliente" :
        cliente = Cliente()
        clienti = session.query(Clienti).filter_by(CodiceFiscale=cliente.t_s.codice_fiscale).all()
        #controllo esistenza cliente nel database
        for cliente in clienti :
            print(" utente già registrato ")
            break
        # creazione profilo utente
        profilo = ProfiloUtente(cliente)
        print(f"""  registrazione effettuata con successo 
                    Benvenuto {profilo.nome_utente} !""")
        session.add(cliente)
        session.commit()
        return profilo

    elif user == "Farmacista" :
        farmacista = Farmacista()
        farmacisti = session.query(Farmacisti).filter_by(matricola =farmacista.t_p.n_matricola).all()
        # controllo esistenza farmacista nel database
        for farmacista in Farmacisti:
            print(" utente già registrato ")
            break
        # creazione profilo utente
        profilo = ProfiloUtente(farmacista)
        print(f"""  registrazione effettuata con successo 
                    Benvenuto {profilo.nome_utente} !""")
        session.add(farmacista)
        session.commit()
        return profilo



#verifica di funzioanmento del codice

controllo = "go"
while controllo != "exit" :
    selezione = input(""" Selezionare il tipo di profilo che si desidera creare ( scrivere una delle seguenti opzioni) :
               -Cliente
               -Farmacista 
               """)

    profilo = registrarsi(selezione)
    controllo = input("controllo")




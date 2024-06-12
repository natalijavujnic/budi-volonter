from mysql import connector
import random
from datetime import datetime

from lokacija import countries
print(countries)
db = connector.connect(
        host='127.0.0.1',
        port='3306',
        password='123',
        database='budivolonter',
        user='root'
    )

# Establish the database connection

cursor = db.cursor()
def reset_autoincrement():
    # Retrieve the names of all tables in the database
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    
    # Iterate through each table and reset the auto-increment value
    for table in tables:
        table_name = table[0]
        reset_query = f"ALTER TABLE `{table_name}` AUTO_INCREMENT = 1"
        cursor.execute(reset_query)
        print(f"Reset auto-increment value for table: {table_name}")

    db.commit()


reset_autoincrement()

def insert_korisnik():
    for i in range(2,100):
        email = f'test{i}@gmail.com'
        password = 'pbkdf2_sha256$720000$fB91HR8EMIQCYYMDbfJEbR$J5KoRCekeUntUSPXc0zTE7fE+dWohcmOXI9sWxm3Dho='
        ime = f'Name{i}'
        prezime = f'Surname{i}'
        pib = random.randint(100000000, 999999999)
        telefon = f'{random.randint(1000000000, 9999999999)}'
        tip = random.choice(['V', 'O'])
        datumRodj = datetime(1990, 1, 1).strftime('%Y-%m-%d')
        last_login = None
        is_active = 0

        query = '''
        INSERT INTO `korisnik` (`email`, `password`, `ime`, `prezime`, `pib`, `telefon`, `tip`, `datumRodj`, `last_login`, `is_active`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (email, password, ime, prezime, pib, telefon, tip, datumRodj, last_login, is_active))

def insert_lokacija():
    for i in range(100):
        drzava = random.choice(countries)
        continents = ['Evropa', 'Azija', 'Afrika', 'Amerika', 'Australija']
        kontinent = random.choice(continents)

        query = '''
        INSERT INTO `lokacija` (`drzava`, `kontinent`)
        VALUES (%s, %s)
        '''
        cursor.execute(query, (drzava, kontinent))

def insert_aktivnost():
    for i in range(100):
        idOrg = random.randint(2, 99)
        naziv = f'Aktivnost{i}'
        brMesta = random.randint(10, 100)
        month = random.choice((6,7))
        datumOd = datetime(2024, month, 1).strftime('%Y-%m-%d')
        datumDo = datetime(2024, month, 10).strftime('%Y-%m-%d')
        datumRok = datetime(2024, 6, 25).strftime('%Y-%m-%d')
        mesto = f'Mesto{i}'
        lokacija = random.randint(1, 99)
        opis = f'Opis{i}'

        query = '''
        INSERT INTO `aktivnost` (`idOrg`, `naziv`, `brMesta`, `datumOd`, `datumDo`, `datumRok`, `mesto`, `lokacija`, `opis`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (idOrg, naziv, brMesta, datumOd, datumDo, datumRok, mesto, lokacija, opis))

def insert_oblast():
    for i in range(100):
        oblast = f'Oblast{i}'

        query = '''
        INSERT INTO `oblast` (`oblast`)
        VALUES (%s)
        '''
        cursor.execute(query, (oblast,))

def insert_prepiska():
    for i in range(100):
        idKor1 = random.randint(2, 99)

        idKor2 = random.randint(2, 99)
        query = '''
        INSERT INTO `prepiska` (`idKor1`, `idKor2`)
        VALUES (%s, %s)
        '''
        cursor.execute(query, (idKor1, idKor2))

def insert_poruka():
    for i in range(1000):
        idPre = random.randint(1, 99)
        redBr = str(i)
        tekst = f'Tekst{i}'
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        status = random.choice(['N', 'R'])
        idSender = random.randint(2, 99)

        query = '''
        INSERT INTO `poruka` (`idPre`, `redBr`, `tekst`, `time`, `status`, `idSender`)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (idPre, redBr, tekst, time, status, idSender))


def insert_prijava():
    for i in range(1000):
        idVol = random.randint(2, 99)
        idAkt = random.randint(2, 99)
        pismo = f'Pismo{i}'
        rezime = None
        status = random.choice(['A', 'R'])
        preporukaVol = random.choice([None, 'Y'])
        preporukaOrg = random.choice([None, 'Y'])
        komVol = f'Komentar Vol{i}'
        komOrg = f'Komentar Org{i}'

        query = '''
        INSERT INTO `prijava` (`idVol`, `idAkt`, `pismo`, `rezime`, `status`, `preporukaVol`, `preporukaOrg`, `komVol`, `komOrg`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (idVol, idAkt, pismo, rezime, status, preporukaVol, preporukaOrg, komVol, komOrg))

def insert_pripada():
    for i in range(1000):
        idAkt = random.randint(1,99)
        idObl = random.randint(1, 99)

        query = '''
        INSERT INTO `pripada` (`idAkt`, `idObl`)
        VALUES (%s, %s)
        '''
        cursor.execute(query, (idAkt, idObl))

def insert_vestina():
    for i in range(1000):
        idAkt = random.randint(1, 99)
        opis = f'Opis{i}'

        query = '''
        INSERT INTO `vestina` (`idAkt`, `opis`)
        VALUES (%s, %s)
        '''
        cursor.execute(query, (idAkt, opis))

def insert_zanima_ga():
    for i in range(1000):
        idKor = random.randint(2, 99)
        idObl = random.randint(1, 99)

        query = '''
        INSERT INTO `zanima_ga` (`idKor`, `idObl`)
        VALUES (%s, %s)
        '''
        cursor.execute(query, (idKor, idObl))

insert_korisnik()
insert_lokacija()
insert_aktivnost()
insert_oblast()
insert_prepiska()
insert_poruka()
insert_prijava()
insert_pripada()
insert_vestina()
insert_zanima_ga()

cursor.close()
db.commit()
db.close()

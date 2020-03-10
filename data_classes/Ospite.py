from dataclasses import dataclass
from PyQt5.QtCore import QDate
from data_classes.MySqlTuple import MySqlTuple
from datetime import date
from decimal import Decimal

ospiti_table_fields = {'id': ('INTEGER', None, 'NOT NULL AUTO_INCREMENT PRIMARY KEY'),
                 'name': ('VARCHAR', 15, 'NOT NULL'),
                 'surname': ('VARCHAR', 15, 'NOT NULL'),
                 'phone': ('VARCHAR', 15, 'NOT NULL'),
                 'email': ('VARCHAR', 30, 'NOT NULL'),
                 'create_on': ('DATE', None, 'NOT NULL'),
                 }
@dataclass
class Ospite:
    # id: MySqlTuple
    # nome: MySqlTuple
    # cognome: MySqlTuple
    # telefono: MySqlTuple
    # email: MySqlTuple
    # prenotazioni: MySqlTuple
    # # data: QDate
    # data: MySqlTuple
    nome: tuple
    cognome: tuple
    telefono: tuple
    email: tuple
    prenotazioni: tuple
    # data: QDatetuple
    data: tuple

if __name__ == '__main__':
    pass
    # osp = Ospiti(nome = 'Lucio',cognome = 'Di Capua', telefono='3343519984')
    osp = Ospite(1, 'Lucio', 'Di Capua', '3343519984', 'lucio.di.capua@gmail.com', [], date.today())
    # pren = Prenotazioni(1,1,date.today(),Decimal(40.00), Decimal(4.00),[date(2020,3,3), date(2020,3,4)])
    # print(osp.__dict__)
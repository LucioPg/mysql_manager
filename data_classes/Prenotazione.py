from dataclasses import dataclass
from PyQt5.QtCore import QDate
from datetime import date
from decimal import Decimal
from data_classes.MySqlTuple import MySqlTuple

prenotazione_table_fields = {'id': ('INTEGER', None, 'NOT NULL AUTO_INCREMENT PRIMARY KEY'),
                 'ospite_id': ('VARCHAR', 15, 'NOT NULL'),
                 'data_creazione': ('VARCHAR', 15, 'NOT NULL'),
                 'importo': ('DECIMAL', 30, 'NOT NULL DEFAULT 0'),
                 'tasse': ('DECIMAL', None, 'NOT NULL DEFAULT 0'),
                 'date_prnt_id': ('INTEGER', None, 'NOT NULL'),  # needs to be referenced
                 }

@dataclass
class Prenotazione:
    id: tuple
    ospite_id: tuple
    data_creazione: tuple
    importo: tuple
    tasse: tuple
    giorni: tuple
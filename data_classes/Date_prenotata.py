from dataclasses import dataclass
from PyQt5.QtCore import QDate
from datetime import date


@dataclass
class DatePrenotata:
    prenotazione_id = tuple
    data = tuple

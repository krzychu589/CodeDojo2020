from dataclasses import dataclass
from datetime import date

@dataclass
class Friend:
    first_name: str
    last_name: str
    email: str
    birth_date: date

from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin


@dataclass
class Court(DataClassJsonMixin):
    id: int
    name: str
    slug: str
    state: int
    level_of_appeal: str
    jurisdiction: str
    city: str


@dataclass
class InputLegalData(DataClassJsonMixin):
    id: int
    slug: str
    court: Court
    file_number: str
    date: str
    created_date: str
    updated_date: str
    type: str
    ecli: str
    content: str

    def __str__(self):
        return f"{self.id} - {self.court.name}"


@dataclass
class OutputLegalData:
    id: str
    slug: str
    court_name: str
    type: str
    content: str

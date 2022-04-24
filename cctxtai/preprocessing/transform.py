from dataclasses import dataclass

from cctxtai.preprocessing.reader import LegalData


@dataclass
class OutputLegalData:
    id: str
    slug: str
    court_name: str
    type: str
    content: str


def transform(data: [LegalData]) -> [dict]:
    return [OutputLegalData(
        id=x.id,
        slug=x.slug,
        court_name=x.court.name,
        type=x.type,
        content=x.content
    ) for x in data]

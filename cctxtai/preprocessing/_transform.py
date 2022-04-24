from cctxtai.preprocessing.types import InputLegalData, OutputLegalData


def transform(data: [InputLegalData]) -> [dict]:
    return [OutputLegalData(
        id=x.id,
        slug=x.slug,
        court_name=x.court.name,
        type=x.type,
        content=x.content
    ) for x in data]

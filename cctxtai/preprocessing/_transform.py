from cctxtai.preprocessing.types import InputLegalData, OutputLegalData


def transform(data: [InputLegalData]) -> [OutputLegalData]:
    return [OutputLegalData(
        id=x.id,
        slug=x.slug,
        court_name=x.court.name,
        type=x.type,
        content=_parase_html(x.content)
    ) for x in data]


def _parase_html(html_string: str) -> str:
    import html2text
    return html2text.html2text(html_string)

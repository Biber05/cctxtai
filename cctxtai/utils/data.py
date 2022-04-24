from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin

from cctxtai.utils import create_logger

DATA_LOG = create_logger("data", "DEBUG")


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
class LegalData(DataClassJsonMixin):
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


class DataGenerator:
    def __init__(self, source_file_path: str):
        from pathlib import Path
        path = Path(source_file_path)
        if not path.exists():
            raise FileNotFoundError(path)
        else:
            self._path = path

    def __call__(self, *args, **kwargs) -> [LegalData]:
        json_data = self._read_json(self._path.__str__())
        DATA_LOG.debug(f"Found JSON data from length: {len(json_data)}")
        data = [self._to_model(json_data)]
        DATA_LOG.debug(f"Transformed {len(data)} JSON to {LegalData.__name__}")
        return data

    @staticmethod
    def _read_json(filename: str) -> str:
        import json
        with open(filename, 'r') as f:
            return json.load(f)

    @staticmethod
    def _to_model(json_data: str) -> LegalData:
        try:
            return LegalData.from_dict(json_data)
        except RuntimeWarning:
            return LegalData.from_dict(json_data, infer_missing=True)

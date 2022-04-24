import json

from cctxtai.preprocessing import PREPROCESSING_LOG
from cctxtai.preprocessing.types import InputLegalData
from cctxtai.utils import timer


class DataGenerator:
    def __init__(self, source_file_path: str):
        from pathlib import Path
        path = Path(source_file_path)
        if not path.exists():
            raise FileNotFoundError(path)
        else:
            self._path = path

    def __call__(self, *args, **kwargs) -> [InputLegalData]:
        max_lines = -1 if "max_lines" not in kwargs.keys() else kwargs.get("max_lines")

        json_data = self._read_json(self._path.__str__(), max_lines=max_lines)
        PREPROCESSING_LOG.debug(f"Found {len(json_data)} JSON objects in {self._path}")

        data = []
        for x in json_data:
            data.append(self._to_model(x))

        PREPROCESSING_LOG.debug(f"Transformed {len(data)} JSON to {InputLegalData.__name__}")
        return data

    @staticmethod
    @timer
    def _read_json(filename: str, max_lines: int = -1) -> [str]:
        data = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            max_lines = max_lines if max_lines != -1 else len(lines)
            for line in lines[:max_lines]:
                data.append(json.loads(line))
        return data

    @staticmethod
    def _to_model(json_data: str) -> InputLegalData:
        try:
            return InputLegalData.from_dict(json_data)
        except RuntimeWarning:
            return InputLegalData.from_dict(json_data, infer_missing=True)

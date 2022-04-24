import pandas as pd

from cctxtai.preprocessing.transform import OutputLegalData


def write_to_parquet(data: [OutputLegalData], output_file_path: str):
    df = pd.DataFrame.from_dict(data)
    df.to_parquet(output_file_path, engine="fastparquet", compression="snappy")

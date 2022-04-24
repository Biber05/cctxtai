import pandas as pd

from cctxtai.preprocessing import PREPROCESSING_LOG
from cctxtai.preprocessing._transform import OutputLegalData


def write_to_parquet(data: [OutputLegalData], output_file_path: str):
    df = pd.DataFrame.from_dict(data)
    df.to_parquet(output_file_path, engine="fastparquet", compression="snappy")
    PREPROCESSING_LOG.info(f"Wrote {len(df)} rows to {output_file_path}")

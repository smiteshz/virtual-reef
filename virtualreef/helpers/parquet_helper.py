from typing import BinaryIO

import pandas as pd


class ParquetHelper(object):

    def __init__(self, file_path: str) -> None:
        self._parquet_file: str = file_path

    @property
    def parquet_file_as_df(self) -> pd.DataFrame:
        return pd.read_parquet(self._parquet_file)

    @property
    def parquet_file_as_bytes(self) -> BinaryIO:
        return open(self._parquet_file, 'rb')

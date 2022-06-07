import os
import pandas as pd


def get_json_reader(BASE_DIR, table_name, chunk_size=1000):
    filename = os.listdir(f'{BASE_DIR}/{table_name}')[0]
    fp = f'{BASE_DIR}/{table_name}/{filename}'
    return pd.read_json(fp, lines=True, chunksize=chunk_size)


if __name__ == "__main__":
    BASE_DIR = os.environ.get('BASE_DIR')
    table_name = os.environ.get('table_name')
    json_reader = get_json_reader(BASE_DIR, table_name)
    for idx, df in enumerate(json_reader):
        print(f'No. of. records in chunk with index {idx} is {df.shape[0]}')
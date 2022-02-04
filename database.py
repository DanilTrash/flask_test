import sqlite3
import pandas as pd


class SqliteData:

    con = sqlite3.connect(r'data.db')


class PandasData:

    def __init__(self, page):
        self.url = (f'https://docs.google.com/spreadsheets/d/12U5G94RRohSdDujUKU70LrS3iCKOOe5rRKfVIGmVaf0/'
                    f'export?format=csv&id=12U5G94RRohSdDujUKU70LrS3iCKOOe5rRKfVIGmVaf0&gid={page}')

    def __call__(self, arg):
        value = pd.read_csv(self.url, dtype={arg: str})[arg]
        return value

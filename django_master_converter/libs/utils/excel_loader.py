from pathlib import Path
from typing import ItemsView
import pandas as pd

class ExcelLoader:
    def __init__(self, file_path) -> None:
        self.excel_data_frame = pd.read_excel(file_path, sheet_name=None, index_col=0, dtype=str)

    def get_converted_data(self) -> dict:
        """
        {table_name1: {field_name1: {}, field_name2: {},...}, 
         table_name2: {field_name1: {}, field_name2: {},...}}
        """
        result = {} 
        for sheet_name in self.excel_data_frame.keys():
            # #から始まるデータを除外 
            # TODO:正規表現で指定できるほうがいいかも?
            if sheet_name.startswith('#'):
                continue

            sheet_data = self.excel_data_frame[sheet_name]
            field_property = {}
            for key, item in sheet_data.iterrows():
                field_name = key if str == type(key) else ''
                if field_name == '':
                    continue

                field_property[field_name] = {
                    'field_type' : item['type'],
                    'blank': item['blank'] if str == type(item['blank']) else '',
                    'null': item['null'] if str == type(item['null']) else '',
                    'length': item['length'] if str == type(item['length']) else '',
                    'default': item['default'] if str == type(item['default']) else ''
                }
            result[sheet_name] = field_property
        return result
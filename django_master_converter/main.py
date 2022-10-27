from pprint import pprint
from cmath import isnan, nan
from dataclasses import field
from pathlib import Path
import math
import argparse
import pandas as pd

from libs.constant.const import Const
from libs.converter.str_to_model_field import ConvertToModelField
from libs.model.class_model import ClassModel
from libs.model.script_model import ScriptModel



from libs.utils.excel_loader import ExcelLoader

class ConvertMain:
    def __init__(self, input_path, output_path):
        if input_path is None:
            self.input_path = Const.MASTER_FILE_PATH
        else:
            self.input_path = Path(input_path)
        if output_path is None:
            self.output_path = Path(Const.CONVER_EXPORT_PATH)
        else:
            self.output_path = Path(output_path)

    def Main(self):
        script_model = ScriptModel()
        excel_loader = ExcelLoader(self.input_path)
        for key, item in excel_loader.get_converted_data().items():
            class_model = ClassModel(key)
            for field_key, field_item in item.items():
                class_model.add_column_field(field_item['field_type'], field_key, field_item['blank'], field_item['null'], field_item['length'], field_item['default'])
            script_model.add_class(class_model)

        script_model.write_script(self.output_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='コンフィグファイルの指定で使用します')
    parser.add_argument('-o', '--output', help='コンフィグファイルの指定で使用します')
    # parser.add_argument('-c', '--config', help='コンフィグファイルの指定で使用します')
    args = parser.parse_args()

    if args.file is None:
        raise ValueError("Need to -f. select inport excel file path")
    if args.output is None:
        raise ValueError("Need to -o. select output file path")

    cm = ConvertMain(args.file, args.output)
    cm.Main()
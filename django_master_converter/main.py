from pprint import pprint
from libs.constant.const import Const
from libs.converter.str_to_model_field import ConvertToModelField
from libs.model.class_model import ClassModel
from libs.model.script_model import ScriptModel

from cmath import isnan, nan
from dataclasses import field
import math
from pathlib import Path
import pandas as pd

from libs.utils.excel_loader import ExcelLoader

class ConvertMain:
    def Main(self):
        script_model = ScriptModel()
        excel_loader = ExcelLoader(Const.MASTER_FILE_PATH)
        for key, item in excel_loader.get_converted_data().items():
            class_model = ClassModel(key)
            for field_key, field_item in item.items():
                class_model.add_column_field(field_item['field_type'], field_key, field_item['blank'], field_item['null'], field_item['length'], field_item['default'])
            script_model.add_class(class_model)

        script_model.write_script(Const.CONVER_EXPORT_PATH)

if __name__ == '__main__':
    cm = ConvertMain()
    cm.Main()
from DjangoMasterConverter.libs.constant.const import Const
from DjangoMasterConverter.libs.converter.str_to_model_field import ConvertToModelField
from cmath import isnan, nan
from dataclasses import field
import math
from pathlib import Path
import pandas as pd

class ConvertMain:
    def _ReadExcel(self) -> dict:
        conv=ConvertToModelField()
        df = pd.read_excel(Const.MASTER_FILE_PATH, sheet_name=None, index_col=0, dtype=str)
        master_map = {}
        for sheet_name in df.keys():
            # #から始まるシートを除外
            if sheet_name.startswith('#'):
                continue

            df_sheet = df[sheet_name]
            fields=[]
            for key, item in df_sheet.iterrows():
                name = key if str == type(key) else ''
                if name == '': # '' or nan の場合処理をスキップ
                    continue

                field_type = item['type']
                blank = item['blank'] if str == type(item['blank']) else ''
                null = item['null'] if str == type(item['null']) else ''
                max_length = item['length'] if str == type(item['length']) else ''
                default = item['default'] if str == type(item['default']) else ''

                fields.append(conv.ConvField(field_type=field_type,name=name,blank=blank,null=null,max_length=max_length,default=default))
            master_map[sheet_name]=fields
        return master_map

    def _MakeClass(self):
        content = Path(Const.CLASS_TEMPLATE_PATH).read_text()
        py_code_text = 'from django.db import models \n\n'
        for key, items in self._ReadExcel().items():
            field_text= ''
            for item in items:
                field_text = field_text + '    ' + item + '\n'
            class_text = content.replace('<MASTER_NAME>', key)
            class_text = class_text.replace('<FIELDS>', field_text)
            py_code_text = py_code_text + class_text + '\n\n'
        
        Path(Const.CONVER_EXPORT_PATH).write_text(py_code_text)


    def Main(self):
        self._MakeClass()
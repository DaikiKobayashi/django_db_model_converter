from dataclasses import field
from pathlib import Path
from libs.model.class_field_model import ClassFieldModel
from libs.constant.const import Const


# テーブルのクラスを管理するモデル
class ClassModel:
    def __init__(self, table_name: str):
        self.table_name = table_name
        self.class_fields = []
    
    def add_column_field(self, field_type: str, column_name:str, blank: str, null: str, max_length:str, default: str):
        field_model = ClassFieldModel(field_type, column_name, blank, null, max_length, default)
        self.class_fields.append(field_model)
    
    def get_class_text(self) -> str:
        class_template = Path(Const.CLASS_TEMPLATE_PATH).read_text()

        export_text = class_template.replace(Const.REPLACE_TAG_TABLE_NAME, self.table_name)
        field_text = ''
        for class_field in self.class_fields:
            field_text += '    ' + class_field.get_field() + '\n'

        export_text = export_text.replace(Const.REPLACE_TAG_CLASS_FIELDS, field_text)
        
        return export_text
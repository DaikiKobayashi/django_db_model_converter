from DjangoMasterConverter.libs.constant.const import Const
from DjangoMasterConverter.libs.model.script_model import ScriptModel

# テーブル内のfieldを管理するモデル
# ここでConvertToModelFieldのfieldMapをへんかんする予定
class ClassFieldModel:
    field=''

# テーブルのクラスを管理するモデル
class ClassModel:
    table_name=''
    table_fields=[]

    def __init__(self, table_name: str):
        self.class_text = ''
    
    def add_column_field(self):
        return
    
    def get_class_text(self):
        return 
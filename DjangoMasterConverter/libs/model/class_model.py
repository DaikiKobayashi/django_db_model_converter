from DjangoMasterConverter.libs.constant.const import Const
from DjangoMasterConverter.libs.model.script_model import ScriptModel
from DjangoMasterConverter.libs.model.class_field_model import ClassFieldModel


# テーブルのクラスを管理するモデル
class ClassModel:
    table_name=''
    table_fields=[]

    def __init__(self, table_name: str):
        self.class_text = table_name
    
    def add_column_field(self, field_type: str, column_name:str, blank: str, null: str, max_length:str, default: str):
        field_model = ClassFieldModel(field_type=field_type,name=column_name,blank=blank,null=null,max_length=max_length,default=default)
        field_model.get_field()
    
    def get_class_text(self):
        return 
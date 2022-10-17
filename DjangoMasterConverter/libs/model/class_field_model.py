from DjangoMasterConverter.libs.converter.str_to_model_field import ConvertToModelField

# テーブル内のfieldを管理するモデル
# ここでConvertToModelFieldのfieldMapをへんかんする予定
class ClassFieldModel:
    field=''

    def __init__(self, field_type: str, name:str, blank: str, null: str, max_length:str, default: str):
        converter = ConvertToModelField()
        field = converter.ConvField(field_type=field_type,name=name,blank=blank,null=null,max_length=max_length,default=default)

    def get_field(self):
        return self.field
from libs.converter.str_to_model_field import ConvertToModelField

from libs.constant.const import Const

# テーブル内のfieldを管理するモデル
# ここでConvertToModelFieldのfieldMapをへんかんする予定
class ClassFieldModel:
    FIELD_TEMPLATE_MAP = {
        "int" : "<NAME> = models.IntegerField(<NULL><BLANK><DEFAULT>)",
        "bigint" : "<NAME> = models.BigIntegerField(<NULL><BLANK><DEFAULT>)",
        "uint" : "<NAME> = models.PositiveIntegerField(<NULL><BLANK><DEFAULT>)",
        "ubigint" : "<NAME> = models.PositiveBigIntegerField(<NULL><BLANK><DEFAULT>)",
        "float" : "<NAME> = models.FloatField(<NULL><BLANK><DEFAULT>)",
        "decimal" : "<NAME> = models.DecimalField(<NULL><BLANK><DEFAULT>)",
        "char" : "<NAME> = models.CharField(<NULL><BLANK><MAX_LENGTH><STR_DEFAULT>)",
        "text" : "<NAME> = models.TextField(<NULL><BLANK><MAX_LENGTH><STR_DEFAULT>)",
        "json" : "<NAME> = models.JSONField(<NULL><BLANK><STR_DEFAULT>)",
        "boolean" : "<NAME> = models.BooleanField(<NULL><BLANK><DEFAULT>)",
        "date" : "<NAME> = models.DateField(<NULL><BLANK><STR_DEFAULT>)",
        "time" : "<NAME> = models.TimeField(<NULL><BLANK><STR_DEFAULT>)",
        "datetime" : "<NAME> = models.DateTimeField(<NULL><BLANK><STR_DEFAULT>)",
    }
    
    field=''

    def __init__(self, field_type: str, name:str, blank: str, null: str, max_length:str, default: str):
        converter = ConvertToModelField()
        field = converter.ConvField(field_type=field_type,name=name,blank=blank,null=null,max_length=max_length,default=default)

    def get_field(self) -> str:
        return self.field
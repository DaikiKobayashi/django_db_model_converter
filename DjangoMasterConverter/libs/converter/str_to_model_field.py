from DjangoMasterConverter.libs.constant.const import Const
from asyncio.windows_events import NULL
from cmath import nan
import json
from pathlib import Path

class ConvertToModelField:
    fieldMap = {
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

    def __init__(self) -> None:
        with Path(Const.CONVERT_CONFIG_PATH).open('r', encoding="utf-8") as config:
            field_dictionary = json.load(config)["field_convert_data"]
            for key, value in field_dictionary.items():
                self.fieldMap[key] = value
        
        config.close

    def _SelectField(field_type: str) -> str:
        select_field = ConvertToModelField.fieldMap[field_type]

        if select_field == NULL:
            raise ValueError("ERROR!")

        return select_field

    def _ReplaceColumnName(field:str, name: str) -> str:
        return field.replace('<NAME>', name)

    def _ReplaceNull(field:str, blank: str) -> str:
        if blank in ['True', 'true', 'yes', 'y']:
            return field.replace('<NULL>', 'null=True')
        return field.replace('<NULL>', 'null=False')

    def _ReplaceBlank(field:str, blank: str) -> str:
        if blank in ['True', 'true', 'yes', 'y']:
            return field.replace('<BLANK>', ', blank=True')
        return field.replace('<BLANK>', '')

    def _ReplaceMaxLength(field:str, blank: str) -> str:
        if blank not in ['']:
            return field.replace('<MAX_LENGTH>', f', max_length={blank}')
        return field.replace('<MAX_LENGTH>', '')

    def _ReplaceDefault(field:str, blank: str) -> str:
        if blank not in ['', NULL, nan]:
            field=field.replace('<DEFAULT>', f', default={blank}')
            field=field.replace('<STR_DEFAULT>',f', default=\'{blank}\'')
            return field
        return field.replace('<DEFAULT>', '').replace('<STR_DEFAULT>','')

    def ConvField(self, field_type: str, name:str, blank: str, null: str, max_length:str, default: str) -> str:
        field = ConvertToModelField._SelectField(field_type=field_type)
        field = ConvertToModelField._ReplaceColumnName(field=field,name=name)
        field = ConvertToModelField._ReplaceNull(field=field,blank=null)
        field = ConvertToModelField._ReplaceBlank(field=field,blank=blank)
        field = ConvertToModelField._ReplaceMaxLength(field=field,blank=max_length)
        field = ConvertToModelField._ReplaceDefault(field=field,blank=default)
        return field
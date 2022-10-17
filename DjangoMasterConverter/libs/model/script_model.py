from DjangoMasterConverter.libs.constant.const import Const
from DjangoMasterConverter.libs.model.class_model import ClassModel

# コード全体を管理するモデル
class ScriptModel:
    master_script_text=''

    def __init__(self):
        self.class_text = 'from django.db import models \n\n'

    def add_class(self, gen_class: ClassModel):
        self.master_script_text = self.master_script_text + "\n" + gen_class.class_text
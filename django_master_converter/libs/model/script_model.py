from libs.model.class_model import ClassModel

from pathlib import Path
from libs.constant.const import Const

# コード全体を管理するモデル
class ScriptModel:
    IMPORT_TEXT = 'from django.db import models \n\n'
    class_models = list[ClassModel]

    def __init__(self):
        pass

    def add_class(self, gen_class: ClassModel):
        print(type(gen_class))
        self.class_models.append(gen_class)

    def write_script(self, write_path: str) -> None:
        write_text = ScriptModel.CLASS_META_TEXT
        for class_model in self.class_models:
            write_text = write_text + class_model.get_class_text + '\n\n'

        Path(write_path).write_text(write_text)
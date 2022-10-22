from libs.model.class_model import ClassModel

from pathlib import Path
from libs.constant.const import Const

# コード全体を管理するモデル
class ScriptModel:
    def __init__(self):
        self.class_models = []

    def add_class(self, gen_class: ClassModel):
        self.class_models.append(gen_class)

    def write_script(self, write_path: str) -> None:
        write_text = Const.IMPORT_TEXT
        for class_model in self.class_models:
            write_text = write_text + class_model.get_class_text() + '\n\n'

        Path(write_path).write_text(write_text)
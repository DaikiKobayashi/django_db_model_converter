from django_master_converter.main import ConvertMain
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', help='コンフィグファイルの指定で使用します')
args = parser.parse_args()

cm = ConvertMain()
cm.Main()
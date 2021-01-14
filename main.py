import argparse
import re
from pathlib import Path

#Parse Arguments
parser = argparse.ArgumentParser(description="Helper Tool Pentru supermarketitalian.ro")
parser.add_argument('--source', default="C:/vsphotos", help="Path-ul catre directorul cu pozele (necesar)")

args = parser.parse_args()

class File():
    def __init__(self, filename):
        self.filename = filename
        self.filename_noext =  Path(self.filename).stem

    def isImage(self):
        ext = [
            'jpg',
            'jpeg',
            'png'
        ]
        if self.filename.split('.')[-1] in ext:
            return True
        return False

    def isMultiple(self):
        regx = re.findall('\((\d)\)', self.filename_noext)
        if bool(regx):
            return True
        return False

    def sku(self):
        regx = re.findall('(?<=\s)(\d+)(?=\s|.)', self.filename_noext)
        if not bool(regx):
            return 0
        return regx[-1]

    def imageCount(self):
        if not self.isMultiple():
            return 1
        return re.findall('\((\d)\)', self.filename_noext)[-1]

    def seoFriendlyName(self):
        return str(self.filename_noext).partition(self.sku())[0]


a = File('aa-bb-cc dd 545656456 (1).jpg')
print(a.sku())
print(a.seoFriendlyName())
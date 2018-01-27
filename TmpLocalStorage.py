# ------------- TmpLocalStorage -------------

from AbstractLocalStorage import *

import os
PRJCT_DIR = '/tmp/RabbitTube'
FILES_DIR = PRJCT_DIR + "/Files"

class TmpLocalStorage(AbstractLocalStorage):
    def __init__(self):
            AbstractLocalStorage.__init__(self)

    def GetCacheDirectory(self):
            return FILES_DIR

    def IsSongInLocalStorage(self, id):
            path = FILES_DIR + '/' + id + '.mp3'
            return os.path.isfile(path)

    def GetFilePath(self, id):
            return FILES_DIR + '/' + id + '.mp3'

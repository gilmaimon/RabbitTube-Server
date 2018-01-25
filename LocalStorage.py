import os
PRJCT_DIR = '/tmp/RabbitTube'
FILES_DIR = PRJCT_DIR + "/Files"

class LocalStorage:
        def __init__(self):
                pass

        def GetCacheDirectory(self):
                return FILES_DIR

        def IsSongInLocalStorage(self, id):
                path = FILES_DIR + '/' + id + '.mp3'
                return os.path.isfile(path)

        def GetFilePath(self, id):
                return FILES_DIR + '/' + id + '.mp3'

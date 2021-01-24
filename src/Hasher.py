import hashlib, os, typing
from args import getArgs

class RecursiveDirectoryHasher():
    def __init__(self, path: str):
        path = os.path.normpath(path)
        if not os.path.isdir(path):
            exit(f'{path} is not directory')
        self.path = path

    def get_hash(self, file: typing.BinaryIO):
        md5,sha1 = hashlib.md5(), hashlib.sha1()
        buf = file.read()
        md5.update(buf)
        file.close()
        sha1.update(buf)
        return md5.hexdigest(), sha1.hexdigest()

    def start(self, callback):
        for path, dirs, files in os.walk(self.path):
            for file in files:
                file = os.path.normpath(path + os.sep + file)
                md5, sha1 = self.get_hash(open(file, 'rb'))
                callback([file, md5, sha1])

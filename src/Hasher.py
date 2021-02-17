import hashlib
import os
import typing


class Hasher():
    def get_hash(self, file: typing.BinaryIO):
        md5, sha1 = hashlib.md5(), hashlib.sha1()
        buf = file.read()
        file.close()
        md5.update(buf)
        sha1.update(buf)
        return md5.hexdigest(), sha1.hexdigest()


class RecursiveDirectoriesHasher(Hasher):
    def __init__(self, path: str):
        path = os.path.normpath(path)
        if not os.path.isdir(path):
            exit(f'{path} is not directory')
        self.path = path

    def start(self, callback):
        for path, dirs, files in os.walk(self.path):
            for file in files:
                file = os.path.join(path, file)
                md5, sha1 = self.get_hash(open(file, 'rb'))
                callback([file, md5, sha1])


class EachDirectoryHasher(Hasher):
    def __init__(self, path: str):
        path = os.path.normpath(path)
        if not os.path.isdir(path):
            exit(f'{path} is not directory')
        self.path = path

    def get_directories_recursive(self, path: str):
        directories = []

        for path, dirs, files in os.walk(path):
            for directory in dirs:
                directories.append(os.path.join(path, directory))

        return directories

    def start(self, callback):
        dirs = self.get_directories_recursive(self.path)
        for dir_index, directory in enumerate(dirs):
            data = []
            for file_index, item in enumerate(os.listdir(directory)):
                item = os.path.join(directory, item)
                if os.path.isfile(item):
                    # serial_number = f'{dir_index + 1}/{file_index + 1}'
                    md5, sha1 = self.get_hash(open(item, 'rb'))
                    data.append({
                        "serial_number": (dir_index, file_index),
                        "file": item,
                        "md5": md5,
                        "sha1": sha1

                    })
            callback(data, directory)

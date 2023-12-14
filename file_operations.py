import os
import hashlib


def copy_file(source_path, replica_path):
    with open(source_path, 'rb') as source_file, open(replica_path, 'wb') as replica_file:
        replica_file.write(source_file.read())


def compare_files(source_file, replica_file):
    with open(source_file, 'rb') as file_to_check:
        data = file_to_check.read()
        source_md5 = hashlib.md5(data).hexdigest()

    with open(replica_file, 'rb') as replica_file_to_check:
        data = replica_file_to_check.read()
        replica_md5 = hashlib.md5(data).hexdigest()

    return source_md5 == replica_md5

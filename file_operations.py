import os
import hashlib
import shutil


def copy_file(source_path, replica_path):
    """copies a file from with the source_path to the replica_path
    if the directory does not exist, it creates it """

    replica_dir = os.path.dirname(replica_path)
    os.makedirs(replica_dir, exist_ok=True)

    shutil.copy2(source_path, replica_path)


def compare_files(source_file, replica_file):
    """compares the source_file md5 with the replica's
    assuring both files have or not the same content
    :returns boolean """

    with open(source_file, 'rb') as file_to_check:
        data = file_to_check.read()
        source_md5 = hashlib.md5(data).hexdigest()

    with open(replica_file, 'rb') as replica_file_to_check:
        data = replica_file_to_check.read()
        replica_md5 = hashlib.md5(data).hexdigest()

    return source_md5 == replica_md5

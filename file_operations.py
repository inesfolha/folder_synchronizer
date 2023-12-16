import os
import hashlib
import shutil
from custom_errors import *


def copy_file(source_path, replica_path):
    """copies a file from with the source_path to the replica_path
    if the directory does not exist, it creates it """

    try:
        replica_dir = os.path.dirname(replica_path)
        os.makedirs(replica_dir, exist_ok=True)

        shutil.copy2(source_path, replica_path)

    except FileNotFoundError:
        raise CopyError(f"Error: The file at {source_path} does not exist.")

    except PermissionError:
        raise CopyError(f"Error: Permission denied. Unable to copy file to {replica_path}")

    except Exception as e:
        raise CopyError(f"An unexpected error occurred: {e}")


def compare_files(source_file, replica_file):
    """compares the source_file md5 with the replica's
    assuring both files have or not the same content
    :returns boolean """
    try:
        with open(source_file, 'rb') as file_to_check:
            data = file_to_check.read()
            source_md5 = hashlib.md5(data).hexdigest()

        with open(replica_file, 'rb') as replica_file_to_check:
            data = replica_file_to_check.read()
            replica_md5 = hashlib.md5(data).hexdigest()

        return source_md5 == replica_md5

    except FileNotFoundError as f:
        raise CompareError(f"Error: One of the files does not exist. Source: {source_file}, Replica: {replica_file}", f)

    except PermissionError as p:
        raise CompareError(f"Error: Permission denied while reading files. Source: {source_file}, Replica: {replica_file}", p)

    except UnicodeDecodeError as u:
        raise CompareError(f"Error: Unable to decode one of the files as text. Source: {source_file}, Replica: {replica_file}", u)

    except IsADirectoryError as d:
        raise CompareError("Error: One or both paths are directories. Please provide valid file paths.", d)

    except Exception as e:
        raise CompareError(f"An unexpected error occurred: {e}")

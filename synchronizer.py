import os
from folder_synchronizer import file_operations
from log_config import configure_logger


class Synchronizer:
    def __init__(self, source_folder_path, replica_folder_path, logger_file):
        self.logger = configure_logger(logger_file)
        self.source_folder_path = source_folder_path
        self.replica_folder_path = replica_folder_path

    def _get_source_files(self):
        """returns a set of all the files in the source folder with the full path"""
        source_files = set()
        for root, dirs, files in os.walk(self.source_folder_path):
            for file in files:
                source_files.add(os.path.join(root, file))
        return source_files

    def _get_replica_files(self):
        """returns a set of all the files in the replica folder with the full path"""
        replica_files = set()
        for root, dirs, files in os.walk(self.replica_folder_path):
            for file in files:
                replica_files.add(os.path.join(root, file))
        return replica_files

    def _get_source_filenames(self):
        """returns a set of the filenames in the source folder"""
        source_files_path = self._get_source_files()
        source_file_names = {os.path.basename(path) for path in source_files_path}
        return source_file_names

    def _get_replica_filenames(self):
        """returns a set of the filenames in the replica folder"""
        replica_files_path = self._get_replica_files()
        replica_file_names = {os.path.basename(path) for path in replica_files_path}
        return replica_file_names

    def _update_common_files(self):
        """ finds all file names common in both folders, compares
        it's content and replaces the ones that have been changed """

        source_file_names = self._get_source_filenames()
        replica_file_names = self._get_replica_filenames()

        common_files = source_file_names.intersection(replica_file_names)

        # compare the common files
        for file_name in common_files:
            source_path = os.path.join(self.source_folder_path, file_name)
            replica_path = os.path.join(self.replica_folder_path, file_name)
            if not file_operations.compare_files(source_path, replica_path):
                file_operations.copy_file(source_path, replica_path)
                self.logger.info(f'File: {file_name} Successfully updated.')

    def _save_missing_files(self):
        """finds all files that exist in the source folder
        but not in the replica and copies them"""

        source_files = self._get_source_filenames()
        replica_files = self._get_replica_filenames()

        # find the files to copy from source to target folder
        missing_files = source_files.difference(replica_files)
        for file in missing_files:
            source_path = os.path.join(self.source_folder_path, file)
            replica_path = os.path.join(self.replica_folder_path, file)
            file_operations.copy_file(source_path, replica_path)
            self.logger.info(f'File: {file} successfully copied to backup.')

    def _remove_extra_files(self):
        """finds all files that exist in the replica folder
                but not in the source and removes them"""
        source_files = self._get_source_filenames()
        replica_files = self._get_replica_filenames()

        extra_files = replica_files.difference(source_files)
        for file in extra_files:
            replica_path = os.path.join(self.replica_folder_path, file)
            os.remove(replica_path)
            self.logger.info(f'File: {file} deleted from backup folder.')

    def synchronize_folders(self):
        self._update_common_files()
        self._save_missing_files()
        self._remove_extra_files()
        self.logger.info('Synchronization complete')


# Log operations to the log_file
test = Synchronizer(r'C:\Users\inesf\OneDrive\Ambiente de Trabalho\source_folder',
                    r'C:\Users\inesf\OneDrive\Ambiente de Trabalho\replica_folder',
                    "logs/log.log")

test.synchronize_folders()

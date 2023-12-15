import os
import file_operations
from log_config import configure_logger


class Synchronizer:
    def __init__(self, source_folder_path, replica_folder_path, log_directory):
        self.changed = False
        self.logger = configure_logger(log_directory)
        self.source_folder_path = source_folder_path
        self.replica_folder_path = replica_folder_path

    def _get_source_filenames(self):
        """returns a set of all the files in the source folder with the full path"""
        source_file_names = set()
        for root, dirs, files in os.walk(self.source_folder_path):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), self.source_folder_path)
                source_file_names.add(relative_path)
        return source_file_names

    def _get_replica_filenames(self):
        """returns a set of all the files in the replica folder with the full path"""
        replica_file_names = set()
        for root, dirs, files in os.walk(self.replica_folder_path):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), self.replica_folder_path)
                replica_file_names.add(relative_path)
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
                self.changed = True

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
            self.changed = True

    def _remove_extra_files(self):
        """finds all files that exist in the replica folder
            but not in the source and removes them"""

        source_files = self._get_source_filenames()
        replica_files = self._get_replica_filenames()

        extra_files = replica_files.difference(source_files)
        for file in extra_files:
            replica_path = os.path.join(self.replica_folder_path, file)

            if os.path.isdir(replica_path): # NOT WORKING
                os.rmdir(replica_path)
                self.logger.info(f'Folder: {file} deleted from backup folder.')
            else:
                os.remove(replica_path)
                self.logger.info(f'File: {file} deleted from backup folder.')
            self.changed = True

    def _check_directories(self):  # FIX THIS
        """checks all the possible directories inside the source folder and synchronizes them"""
        source_file_names = self._get_source_filenames()
        replica_file_names = self._get_replica_filenames()

        for file in source_file_names:
            source_path = os.path.join(self.source_folder_path, file)
            # if we find a folder
            if os.path.isdir(source_path):
                # check if the folder already exists in replica
                if file not in replica_file_names:
                    os.mkdir(os.path.join(self.replica_folder_path, file))
                    self.changed = True

                replica_path = os.path.join(self.replica_folder_path, file)
                sub_synchronizer = Synchronizer(source_path, replica_path, self.logger)
                sub_synchronizer.synchronize_folders()

    def synchronize_folders(self):
        self.changed = False

        self._update_common_files()
        self._save_missing_files()
        self._remove_extra_files()
        # self._check_directories() NOT WORKING

        if self.changed:
            self.logger.info('Synchronization complete')
        else:
            self.logger.info('No changes detected')

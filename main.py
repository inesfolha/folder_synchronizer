import time
from synchronizer import Synchronizer
from set_command_line_args import parse_arguments
from log_config import configure_logger
from custom_errors import *


def main():
    args = parse_arguments()

    source_folder = args.source_folder
    replica_folder = args.replica_folder
    synchronization_interval = args.interval
    log_file = args.log_file

    main_logger = configure_logger(log_file)
    try:
        # Initialize the Synchronizer object with command line arguments
        synchronizer = Synchronizer(source_folder, replica_folder, log_file)

        while True:
            synchronizer.synchronize_folders()
            time.sleep(synchronization_interval)

    except KeyboardInterrupt:
        main_logger.info("KeyboardInterrupt. Synchronization Stopped.")
    except FolderNotFoundError as e:
        main_logger.error(str(e))
    except IsADirectoryError as ia:
        main_logger.error(str(ia))


if __name__ == "__main__":
    main()

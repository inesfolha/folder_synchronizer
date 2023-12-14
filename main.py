import time
from synchronizer import Synchronizer
from set_command_line_args import parse_arguments
from log_config import configure_logger


def main():
    args = parse_arguments()

    source_folder = args.source_folder
    replica_folder = args.replica_folder
    synchronization_interval = args.interval
    log_file = args.log_file

    logger = configure_logger(log_file)

    # Initialize the Synchronizer object with command line arguments
    synchronizer = Synchronizer(source_folder, replica_folder, log_file)
    try:
        while True:
            synchronizer.synchronize_folders()
            time.sleep(synchronization_interval)

    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt. Synchronization Stopped.")


if __name__ == "__main__":
    main()

# python main.py r'C:\Users\inesf\OneDrive\Ambiente de Trabalho\source_folder' r'C:\Users\inesf\OneDrive\Ambiente de Trabalho\replica_folder' 25 "logs/log.log"

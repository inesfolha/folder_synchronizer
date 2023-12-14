import schedule
import time
from synchronizer import Synchronizer
from set_command_line_args import parse_arguments

timer = pass # ARGUMENTS TO GET FROM COMMAND LINE
def main():
    args = parse_arguments()
    test = Synchronizer(r'C:\Users\inesf\OneDrive\Ambiente de Trabalho\source_folder',
                        r'C:\Users\inesf\OneDrive\Ambiente de Trabalho\replica_folder',
                        "logs/log.log") # ARGUMENTS TO GET FROM COMMAND LINE
    while True:
        test.synchronize_folders()
        time.sleep(timer)

if __name__ == "__main__":
    main()

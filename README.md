# Synchronizer 📁
<p id="top"></p>

## Description
Synchronizer is a program that synchronizes two folders: source and replica, maintaining an identical copy of source folder at replica folder:

- Synchronization works one-way: after the synchronization, the content of the
replica folder is modified to exactly match content of the source
folder;
- Synchronization is performed periodically within an interval of seconds set by the user.
- File creation/copying/removal operations are logged to a file and to the
console;
- Errors are logged to a file and to the console with custom messages.
- Folder paths, synchronization interval and logs directory should be provided
using the command line arguments;
- If the replica folder with the specified path does not exist, one will be created.


------------------------------------------------------------------
## How to use
Start by cloning this project or downloading it as Zip.

### Dependencies

To run this project you need Python3 installed with the following dependencies: 

 - argparse
 - logging
 - hashlib
 - shutil
 - os
 - time

Most of these dependencies are built in Python but if for some reason you don't have any installed, you can simply go to the project directory in the command line and run:

```bash
pip install libraryname
```
or
```bash
pip3 install libraryname
```
[Back to the Top](#top)
### Running the Program

To run the program, open a command line terminal and navigate to the directory containing the `main.py` file. Use the following command format to execute the program:

```bash
# On Windows
python main.py --source "C:\path\to\source\folder" --replica "C:\path\to\replica\folder" --interval 30 --log_folder "logs"
```
```bash
# On Linux or MacOS
python3 main.py --source "path/to/source/folder" --replica "path/to/replica/folder" --interval 30 --log_folder "logs"
```
Replace the following placeholders with your specific values

- path/to/source/folder: The full path to the source folder you want to synchronize.
- path/to/replica/folder: The full path to the replica folder where changes will be mirrored.
- 60: The synchronization interval in seconds. Adjust this value according to your synchronization requirements.
- logs: The directory where log files will be stored. Modify this as needed.

### Stopping the Program
To stop the program, press Ctrl + C in the terminal. This will send a keyboard interrupt signal to the program, gracefully stopping its execution.

[Back to the Top](#top)
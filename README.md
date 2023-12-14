# Synchronizer

## Description
This is a program that synchronizes two folders: source and replica, maintaining an identical copy of source folder at replica folder:

- Synchronization works one-way: after the synchronization, the content of the
replica folder is modified to exactly match content of the source
folder;
- Synchronization is performed periodically
- File creation/copying/removal operations are logged to a file and to the
console output;
- Folder paths, synchronization interval and log file path should be provided
using the command line arguments;

------------------------------------------------------------------

import os
import ctypes
import sys

# Define the necessary Windows API constants
SHERB_NOCONFIRMATION = 0x00000001
SHERB_NOPROGRESSUI = 0x00000002
SHERB_NOSOUND = 0x00000004

# Load the Windows Shell32 library
shell32 = ctypes.windll.shell32

def empty_recycle_bin():
    result = shell32.SHEmptyRecycleBinW(None, None, SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND)
    if result == 0:
        print("Recycle Bin emptied successfully.")
    else:
        print("Failed to empty Recycle Bin. Error code:", result)

if __name__ == "__main__":
    if sys.platform == "win32":
        empty_recycle_bin()
    else:
        print("This script is only for Windows systems.")
# LGA UTF-pyCleaner

## Description

LGA UTF-pyCleaner is a tool designed to remove accents, replace the letter 'ñ' with 'n', and normalize other special characters in Python (.py) files. It processes all .py files in a specified directory, including its subdirectories.

## Files

1. `+LGA_UTF-pyCleaner.py`: The main Python script that performs the cleaning operation.
2. `+LGA_UTF-pyCleaner.bat`: A Windows batch file for easy execution of the Python script.

## Requirements

- Python 3.x installed on your system
- Windows operating system (for using the .bat file)

## How to Use

### Method 1: Using the Batch File (Windows only)

1. Ensure Python is installed and added to your system's PATH.
2. Drag and drop the folder you want to process onto the `+LGA_UTF-pyCleaner.bat` file.
3. The script will run automatically, processing all .py files in the dropped folder and its subdirectories.

### Method 2: Running the Python Script Directly

1. Open a command prompt or terminal.
2. Navigate to the directory containing the `+LGA_UTF-pyCleaner.py` file.
3. Run the script with a directory path as an argument:
   ```
   python +LGA_UTF-pyCleaner.py "path/to/your/directory"
   ```
   If no argument is provided, the script will process the directory it's located in.

## What the Script Does

- Scans all .py files in the specified directory and its subdirectories.
- Removes accents from characters (e.g., á -> a, é -> e, ü -> u).
- Replaces 'ñ' with 'n' and 'Ñ' with 'N'.
- Normalizes other special characters to their closest ASCII equivalents.
- Displays which files were modified and shows the specific changes made to each file.

## Note

- The script will not modify itself to prevent unintended alterations.
- Always backup your files before running this script on important code.
- The script preserves the original encoding of the files (UTF-8).

## Version

Current version: 1.2 (2024)

## Author

Lega

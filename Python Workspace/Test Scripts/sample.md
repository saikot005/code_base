# Sample Markdown

This is a sample Markdown file created in the AI Automations folder.

## Details about ai_folder_sizes.py

- Purpose: This script scans a folder path and shows how large its subfolders or contents are.
- Default target: If no path is provided, it uses the D: drive by default.
- Main functions:
  - `get_folder_stats(folder_path)`: Recursively calculates the total size and number of files inside a folder.
  - `get_entry_size(entry_path)`: Returns the size of a file or a folder.
  - `format_size(size_bytes)`: Converts bytes into readable units like KB, MB, GB, and TB.
  - `display_folder_sizes(target_path)`: Prints a sorted list of folders or files with their sizes.
- Behavior:
  - If the target path has subfolders, it lists each subfolder with its total size and file count.
  - If it has no subfolders, it lists the files and folders inside it.
  - It skips inaccessible files or folders caused by permission issues.


## Features
- Easy to read
- Supports headings and lists
- Great for documentation
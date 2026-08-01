import os
import sys

# ─────────────────────────────────────────────
#  Configuration
# ─────────────────────────────────────────────
DRIVE = r"D:\\"  # Essential (D) drive


def get_folder_stats(folder_path: str) -> tuple[int, int]:
    """Recursively calculate total size and file count of a folder."""
    total_size = 0
    file_count = 0

    try:
        with os.scandir(folder_path) as entries:
            for entry in entries:
                try:
                    if entry.is_file(follow_symlinks=False):
                        total_size += entry.stat(follow_symlinks=False).st_size
                        file_count += 1
                    elif entry.is_dir(follow_symlinks=False):
                        sub_size, sub_count = get_folder_stats(entry.path)
                        total_size += sub_size
                        file_count += sub_count
                except (PermissionError, OSError):
                    pass
    except (PermissionError, OSError):
        pass

    return total_size, file_count


def get_entry_size(entry_path: str) -> int:
    """Return the size of a file or a folder recursively."""
    if os.path.isfile(entry_path):
        return os.path.getsize(entry_path)
    return get_folder_stats(entry_path)[0]


def format_size(size_bytes: float) -> str:
    """Convert bytes to a human-readable string (KB, MB, GB, TB)."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"


def display_folder_sizes(target_path: str) -> None:
    """List subfolders or contents of a path sorted by size."""
    if not os.path.exists(target_path):
        print(f"[ERROR] Path '{target_path}' not found.")
        sys.exit(1)

    print("=" * 85)
    print(f"  Folder Sizes  --  {target_path}")
    print("=" * 85)

    try:
        entries = list(os.scandir(target_path))
    except PermissionError:
        print(f"[ERROR] Permission denied accessing '{target_path}'.")
        sys.exit(1)

    subfolders = [entry for entry in entries if entry.is_dir(follow_symlinks=False)]

    if not subfolders:
        print(f"  {'NAME':<35} {'SIZE':>20} {'TYPE':>10}")
        print("-" * 85)

        contents = []
        for entry in entries:
            try:
                if entry.is_file(follow_symlinks=False):
                    size = entry.stat(follow_symlinks=False).st_size
                    kind = "FILE"
                elif entry.is_dir(follow_symlinks=False):
                    size = get_folder_stats(entry.path)[0]
                    kind = "DIR"
                else:
                    continue

                contents.append((entry.name, size, kind))
            except (PermissionError, OSError):
                pass

        contents.sort(key=lambda item: item[1], reverse=True)

        if not contents:
            print("  No contents found in this path.")
        else:
            for name, size, kind in contents:
                print(f"  {name:<35} {format_size(size):>20} {kind:>10}")
    else:
        print(f"  {'FOLDER NAME':<35} {'SIZE':>20} {'FILE COUNT':>15}")
        print("-" * 85)

        folder_data = []
        for folder in subfolders:
            print(f"  Calculating: {folder.name:<30}", end="\r")
            size, file_count = get_folder_stats(folder.path)
            folder_data.append((folder.name, size, file_count))

        folder_data.sort(key=lambda x: x[1], reverse=True)

        for name, size, file_count in folder_data:
            print(f"  {name:<35} {format_size(size):>20} {file_count:>15,}")

    print("=" * 85)
    print(f"  Total items scanned : {len(entries)}")
    print("=" * 85)


if __name__ == "__main__":
    target_path = sys.argv[1] if len(sys.argv) > 1 else DRIVE
    display_folder_sizes(target_path)

from pathlib import Path
import shutil

def traverse_directory(source_dir: Path, dist_dir: Path):
    file_counter = 0

    if not source_dir.is_dir():
        raise ValueError("Source directory does not exist or directory name is incorrect")

    for item in source_dir.iterdir():
        if item.is_dir():
            traverse_directory(item, dist_dir)
        elif item.is_file():
            extension = item.suffix.lstrip('.') or 'no_ext'
            target_dir = dist_dir / extension

            try:
                target_dir.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                raise RuntimeError(f"Failed to create directory {target_dir}: {e}")

            try:
                shutil.copy(item, target_dir)
                print(f"Copied {item} to {target_dir}")
                file_counter += 1
            except Exception as e:
                raise RuntimeError(f"Failed to copy file {item} to {target_dir}: {e}")

    print(f"{file_counter} files copied to {dist_dir}")

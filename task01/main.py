import sys
from pathlib import Path
from traverse_directory import traverse_directory

DESTINATION_DIR = 'dist'

def main():
    try:
        if len(sys.argv) != 2 and len(sys.argv) != 3:
            raise ValueError("Invalid number of arguments")
        elif len(sys.argv) == 2:
            dist_dir = Path(DESTINATION_DIR)
        elif len(sys.argv) == 3:
            dist_dir = Path(sys.argv[2])

        src_dir = Path(sys.argv[1])

        traverse_directory(src_dir, dist_dir)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
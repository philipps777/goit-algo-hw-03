import shutil
import argparse
from pathlib import Path


def copy_files(source_file, destination_dir):
    destination_path = Path(destination_dir)
    file_name = source_file.name
    extension = source_file.suffix.lower()
    dest_subdir = destination_path / extension.strip('.')

    if not dest_subdir.exists():
        dest_subdir.mkdir(parents=True, exist_ok=True)

    try:
        shutil.copy2(source_file, dest_subdir)
    except (shutil.Error, IOError) as e:
        print(f"Error copying file {source_file}: {e}")


def recursive_copy(source_dir, destination_dir):
    source_path = Path(source_dir)
    for item in source_path.iterdir():
        if item.is_dir():
            recursive_copy(item, destination_dir)
        else:
            copy_files(item, destination_dir)


def main():
    parser = argparse.ArgumentParser(
        description="Recursively copies files and sorts them by extension in another directory")
    parser.add_argument("source_dir", type=Path, help="Source directory")
    parser.add_argument("destination_dir", type=Path, nargs='?', default=Path(
        'dist'), help="Destination directory (default is dist)")
    args = parser.parse_args()

    source_dir = args.source_dir
    destination_dir = args.destination_dir

    if not destination_dir.exists():
        destination_dir.mkdir(parents=True, exist_ok=True)

    recursive_copy(source_dir, destination_dir)
    print("Done! Files copied and sorted!")


if __name__ == "__main__":
    main()

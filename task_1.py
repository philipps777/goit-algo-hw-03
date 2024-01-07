import os
import shutil


def copy_files(first_path, given_path):

    if not os.path.exists(first_path):
        print(f"Directory {first_path} is absent.")
        return

    if not os.path.exists(given_path):
        os.makedirs(given_path)

    for item in os.listdir(first_path):
        item_path = os.path.join(first_path, item)
        given_item_path = os.path.join(given_path, item)

        if os.path.isdir(item_path):
            copy_files(item_path, given_item_path)

        elif os.path.isfile(item_path):
            shutil.copy2(item_path, given_item_path)
            print(f"File copied: {item_path} -> {given_item_path}")
        else:
            print(f"Unknown element: {item_path}")


first_directory = r"E:\path"
given_directory = r"C:\destination"

copy_files(first_directory, given_directory)

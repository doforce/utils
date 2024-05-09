from os import rename, listdir
import os.path as path
import argparse

parser = argparse.ArgumentParser(description="Rename WireGuard config file")
parser.add_argument("-d", "--directory",
                    help="Directory where your files locate", required=True)
args = parser.parse_args()

folder_path = args.directory

if not path.isdir(folder_path):
    print(f"{folder_path} not exits")
    exit(1)


for filename in listdir(folder_path):
    if "-" in filename:
        new_filename = filename.replace("-", "")
        old_filepath = path.join(folder_path, filename)
        new_filepath = path.join(folder_path, new_filename)
        rename(old_filepath, new_filepath)

print("Done")

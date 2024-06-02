import argparse
import os
import re
from time import time

start_time = time()

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory",
                    help="Directory where your files locate")
args = parser.parse_args()

folder_path = args.directory
in_same_path = False
if not folder_path:
    folder_path = os.getcwd()
    in_same_path = True

if not os.path.isdir(folder_path):
    print(f"{folder_path} not exits")
    exit(1)

files: list[str] = os.listdir(folder_path)
# filter files
files = list(filter(lambda x: not x.endswith(".py"), files))


for filename in files:
    ext = filename.split(".").pop()
    pattern = r"EP(\d+)"
    match = re.search(pattern, filename)
    if match:
        num = match.group(1)
    else:
        print(filename, "failed")
        continue
    new_filename = f"EP{num}_1080P.{ext}"
    os.rename(os.path.join(folder_path, filename,),
              os.path.join(folder_path, new_filename))
    print(filename, ">", new_filename)

cost = (time() - start_time) * 1000
print(f"COST: {cost:.2f} ms")

if in_same_path:
    input("Press `Enter` to exit...")

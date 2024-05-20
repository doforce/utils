import argparse
import shutil
import os
from time import time

start_time = time()

parser = argparse.ArgumentParser(description="Rename WireGuard config file")
parser.add_argument("-d", "--directory",
                    help="Directory where your files locate", required=True)
args = parser.parse_args()

folder_path = args.directory

if not os.path.isdir(folder_path):
    print(f"{folder_path} not exits")
    exit(1)

files: list[str] = os.listdir(folder_path)
files = list(filter(lambda x: x.endswith(".conf"), files))

REGION_DICT = {
    "NL": "1NL",
    "US": "2US",
    "JP": "3JP"
}

SORTED_DIR = os.path.join(folder_path, "sorted")

if os.path.exists(SORTED_DIR):
    shutil.rmtree(SORTED_DIR)

os.mkdir(SORTED_DIR)


for filename in files:
    wg, region, _, id = filename.split("-")
    new_filename = wg + REGION_DICT[region] + id
    shutil.copyfile(os.path.join(folder_path, filename),
                    os.path.join(SORTED_DIR, new_filename))

cost = (time() - start_time) * 1000
print(f"COST: {cost:.2f} ms")

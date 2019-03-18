import os
import json
import argparse

parser = argparse.ArgumentParser(description='Accept file paths')
parser.add_argument('-f', '--files', help='file paths to ipynb files', required=True, nargs='*')
args = parser.parse_args()

for file_path in args.files:
    
    real_path = os.path.realpath(file_path)
    base_name = os.path.basename(real_path)
    dir_name = os.path.dirname(real_path)
    
    try:
        with open(real_path, 'r') as fp:
            ipynb_data = json.load(fp)
    
    except ValueError:
        print(f"could not load {base_name} from {real_path}")
        continue

    try:
        with open(os.path.join(dir_name, base_name.split('.')[0] + 'corrected.' + base_name.split('.')[1]), 'w') as fp:
            json.dump(ipynb_data, fp, indent=4)
    
    except ValueError:
        print(f"could not dump corrected {base_name} to {sir_name}")
        continue

        

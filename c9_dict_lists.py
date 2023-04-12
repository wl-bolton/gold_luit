#!/usr/bin/env python3.7

import os 

file_list = [] 
cwd = os.getcwd()

for file_name in os.listdir(cwd): 
    file_info = {
        "name": file_name,
        "size": os.path.getsize(file_name),
        "path": os.path.join(cwd, file_name)
    }

    file_list.append(file_info)

for file in file_list:
    print("Name:", file["name"])
    print("Size:", file["size"])
    print("Path:", file["path"], "\n")
#!/usr/bin/env python3.7

#Import module for file information
import os 

# Create an empty list to store file information
file_list = [] 

# Get the current working directory
cwd = os.getcwd()


#Create dictionary with file name, size and path
for file_name in os.listdir(cwd): 
    file_info = {
        "name": file_name,
        "size": os.path.getsize(file_name),
        "path": os.path.join(cwd, file_name)
    }

#Append dictionary info to list
    file_list.append(file_info)

#Loop through file list and print file information
for file in file_list:
    print("Name:", file["name"])
    print("Size:", file["size"])
    print("Path:", file["path"], "\n")
    
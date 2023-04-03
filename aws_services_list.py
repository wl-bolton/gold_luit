#!/usr/bin/env python3

#Create a list of services using Python. IE: S3, Lambda, EC2, etc
# The list should be empty initially.

aws_services = []

# Populate the list using append or insert.

aws_services.append('EC2')
aws_services.append('RDS')
aws_services.append('S3')
aws_services.append('Lambda')
aws_services.append('Cognito')

# Print the list and the length of the list.

length = len(aws_services)
print(aws_services)
print("The list contains " + str(length) + " popular AWS services.")

# Remove two specific services from the list by name or by index.

del aws_services[0]
del aws_services[0]

# Print the new list and the new length of the list.

length = len(aws_services)
print(aws_services)
print("The list contains " + str(length) + " popular AWS services.")

# Push your code to GitHub and include the link in your LinkedIn write up.
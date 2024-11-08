import os

user_id = 900
# Specify the path to the file
file_path = f'../data/users/{user_id}_transactions.csv'

# Check if the file exists
if os.path.isfile(file_path):
    print(f"The file {file_path} exists.")
else:
    print(f"The file {file_path} does not exist.")
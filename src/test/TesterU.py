# import os
# for dirpath, dirnames, filenames in os.walk('C:\Users\Osa\Documents\Codes\Assignment\project\src\data\users')




import re



while True:
    user_exp = input("Enter an expense (or 'q' to finish): £")
    if user_exp.lower() == 'q':
        break  # Breaks the loop if the user is done entering expense

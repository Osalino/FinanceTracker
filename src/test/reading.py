import csv

from src.finance_tracker.personalF import write

fname = input("Enter first name: ")
lname = input("Enter last name")
Door_num = input("Enter last name")

#
# d = open('database.txt','a')
# d.write("\n")
# d.write(fname)
# d.write(" ")
# d.write(lname)
# d.write("\n")
# d.close()
#
#
# d = open('database.txt','r')
# print(d.read())

with open('finance21.csv','a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Last Name","Door Number"]) # Creates a Row
    writer.writerow([fname, lname, Door_num])


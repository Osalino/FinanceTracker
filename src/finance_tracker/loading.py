import os
from time import sleep

# msg = "Loading."
# for x in range(5):
#   msg = msg + "."
#   print(msg)
#   sleep(1)
#   os.system("cls")
#
# print("%sGoodBye!" % msg)
#

def endscreeen():
  msg = "Exciting."
  for x in range(5):
    msg = msg + "."
    print(msg)
    sleep(1)
    os.system("cls")

  print("%sGoodBye!" % msg)

endscreeen()
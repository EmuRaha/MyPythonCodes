#Input a filename and print the extension of that

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print(f_extns)
print ("The extension of the file is : " + repr(f_extns[1]))

print(f_extns[1])

#Get the Python version

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

#date-time

import datetime

now = datetime.datetime.now()
print(now)
import os

def shutdown():
    os.system("shutdown now")

def sleep():
    os.system("systemctl suspend")

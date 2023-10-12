import os

directory=input("Enter the directory name :")
def recv_scan(directory):
    for items in os.listdir(directory):
        file1 = os.path.join(directory,items)
        print(file1)
        if os.path.isdir(file1):
            recv_scan(file1)

recv_scan(directory)
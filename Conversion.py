from imports import *


def toExcel(file):
    print(file)

def toWord(file):
    try:
        with open(file, 'r') as f:
            print("Reading file")
    except Exception as e:
        print("File not found")
        print(e)
from argparse import FileType
from imports import *

def checkFile(file):
    name, extention = os.path.splitext(file)
    if extention != '.pdf':
        raise Exception
    else:
        pass
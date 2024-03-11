import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--path', help= 'paste path to biog.txt file')
args = parser.parse_args()


os.chdir(args.path) # to change directory to argument passed for '--path'

print (os.getcwd())
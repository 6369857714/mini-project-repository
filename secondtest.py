import argparse

parser = argparse.ArgumentParser(description='read the file')

parser.add_argument('--file_path', type=str , dest="file_path")
args = parser.parse_args()
print(args.file_path)

# with args.file as file:
#     data=file.tolist()
#     print(file(0).read())
    
    


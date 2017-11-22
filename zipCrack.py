import zipfile
import argparse
from threading import Thread

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--zipfile', help='the location of zip folder you wish to crack')
parser.add_argument('-d', '--dictionary', help='the location of the dictionary you would like to use to crack the zip folder', type=str)
args = parser.parse_args()

if not (args.dictionary and args.zipfile):
    parser.print_help()
    exit(0)

def extractFile(zFile, password):
    bpass = password.encode('utf-8')
    try:
        zFile.extractall(pwd=bpass)
        print('[+] Password = ' + password)
    except Exception as e:
        pass

def main(dict_location, zip_location):
    zFile = zipfile.ZipFile(zip_location)
    passFile = open(dict_location)

    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
        
if __name__ == '__main__':
    main(args.dictionary, args.zipfile)

import zipfile
from threading import Thread

def extractFile(zFile, password):
    bpass = password.encode('utf-8')
    try:
        zFile.extractall(pwd=bpass)
        print('[+] Password = ' + password)
    except Exception as e:
        pass

def main():
    zFile = zipfile.ZipFile("./evil.zip")
    passFile = open('./dictionary.txt')

    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))

        t.start()
        
if __name__ == '__main__':
    main()

import zipfile

def extractFile(zFile, password):
    bpass = password.encode('utf-8')
    try:
        zFile.extractall(pwd=bpass)
        return True
    except Exception as e:
        return False


def main():
    zFile = zipfile.ZipFile("./evil.zip")
    passFile = open('./dictionary.txt')

    for line in passFile.readlines():
        password = line.strip('\n')
        extracted = extractFile(zFile, passowrd)

        if extracted:
            print('[+] Password = ' + password + '\n')
            exit(0)

        
if __name__ == '__main__':
    main()

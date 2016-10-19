#/usr/bin/python

import itertools
from itertools import islice
import zipfile
from zipfile import ZipFile
import collections

maxVal = 4
minVal =3

zfile = zipfile.ZipFile('ex4_4.zip', 'r')

def main():
    for i, p in enumerate(createDict()):
        try:
            print('Working on it...\n')
            #if do not use pwd=...it will output can create files on the host
            zfile.extractall(pwd=p)
            exit(0)
        except Exception as e:
            pass

#dictionaryList = createDict()
#print(dictionaryList)

def createDict():
    global maxVal
    while maxVal >= minVal:
        wordList = itertools.product('abcdefghijklmnopqrstuvwxyz1234567890!@#', repeat=maxVal)
        maxVal -=1
        for i in wordList:
            yield ''.join(i)

if __name__ == "__main__":
    main()





'''
OTHER JUNK

def main(file):
    zfile = zipfile.ZipFile(file, 'r')
    start = time.time()
    print('Start crack at {}'.format(time.strftime('%j: %H:%M:%S', time.localtime(start))))
        for i, p in enumerate(gen_pass(maxval=4)):
            if not i % 1000: print('.', end='')
            if not i % 100000: print('\n()'.format(i / 100000), end='')
        try:
            zfile.extractall(pwd=p)
            print('\nThe password is {}'.format (p))
            print('That took {} seconds'.format(time.time()-start))
            exit(0)
        except RuntimeError:
                pass
        except Exception as e:
            pass




def genpass(minval=3, maxval=4):
        letters=string.ascii_lowercase
        numbers='0123456789'
        symbols='!@#'
        characters=list(letters) + list(numbers) + list(symbols)
        while maxval >= minval:
            for p in itertools.product(characters, repeat=maxval):
            yield ''.join(p)
        maxval -= 1


'''
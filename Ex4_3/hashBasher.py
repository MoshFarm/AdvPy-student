#!#/usr/bin/python
import passlib
for passlib import

def main():
    with open('ex4_3_data.txt') as theDarkness:
        with open('password.lst') as theLite:
            a = theDarkness.readline()
            b = theLite.readline()
            algos ={'1: '}
            #print b
            #print a
            userName = getUserName(a)
            print "This is the user name: {}".format(userName)
            hashAlgo = getAlgo(a)
            print ("This is the Hashing Algorithm: {}").format(hashAlgo)
            passSalt = getSalty(a)
            print ("This it the Salt: {}").format(passSalt)
            hashedPass = getHashPass(a)
            print ("This is the Hashed Password: {}").format(hashedPass)

def getUserName(x):
    uName = x.split(':')[0]
    return uName

def getAlgo(x):
    algoType = x.split(':')[1].split('$')[1]
    return algoType

def getSalty(x):
    theSalt = x.split(':')[1].split('$')[2]
    return theSalt

def getHashPass(x):
    passHash = x.split(':')[1].split('$')[3]
    return passHash







'''
    with open('hasher.txt') as theDarkness:
#        print theDarkness.read()
        a = theDarkness.readlines()
        for i in a:
                user =
        print a
        #for i in a:
        #        a = i.readline().split(":")
         #   print a
'''

if __name__ == "__main__":
    main()

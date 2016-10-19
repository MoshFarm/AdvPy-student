#!/usr/bin/python

#This program will attempt to crack passwords from a unix shadow file

import crypt

def main():
    crack()

def crack():

    for d in open('ex4_3_data.txt', 'r'):
    #print d
        if '*' in d.split(':') or '!' in d.split(':'):
            pass
        else:
            e = d.split(':')
            f = e[1].split('$')
            i = 0
            for g in open('password.lst', 'r'):
                i = i + 1
                if i % 1000 == 0:
                    print i
                h = crypt.crypt(g.strip(), ''.join(["$", f[1], "$", f[2], "$"]))
                if h.split('$')[3] == f[3]:
                    print "Password cracked for {} - {} after {} attempts".format(e[0], g, i)


if __name__ == '__main__':
    main()
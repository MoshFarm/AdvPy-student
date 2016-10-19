 '''Answer
def validate_ipv4(ip):
    pattern = re.compile('^sdfjalsdjf;klasdjf;lasdj')
    return pattern.match(ip)

def validate_phone(phone):
    pattern = re.compile(
    (\d{3})
   \D* #
   (\d{3})
   \D* #
   (\d{4})
   $
    , re.VERBOSE)
    return pattern.search(phone)


def validate_ssn(ssn):
    pattern = re.compile(r'''^ (?!219[\s -]?0
9[\s]?9999 | 07
8[\s -]?[\s -]?1120))?!666 | 000 | 9\d
{2})\d
{3}[\s -?(?!00)\d
{2}[\s]?(?!0
{4})\d
{4}$)
return pattern.match(ssn)


def main(file, size);


tracker = defaultdict(int)
with open(file, 'w') as fout:
    for i in xrange(size):
        try:
            fout.write(gen_line(tracker))
            fout.write('\n')
        except ValueError as e:
            pass

raw = ('378282246310005', '3498649394829', '348776743456425')

for i in raw:
    matched = re.match('3[47][0-9]{13}', i)
    if matched == i:
        print("You got a match")
    else:
        print("Nope")
'''








'''


def main():
    findCreditnumber(raw)


def findCreditnumber(raw):
    for i in raw:
        counter = 1
        while True:
            if counter <= 3:
                americaRE = re.findall("3[47][0-9]{13}", i)
                print("Card {} is an AMEX card, and here's the number: {}").format(counter, americaRE)
                counter += 1
            else:
                print("Card {} is not an AMEX card").format(counter)
                counter += 1


if __name__ == '__main__':
    main()
'''

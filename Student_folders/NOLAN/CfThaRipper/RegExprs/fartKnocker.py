target_ip = raw_input("Enter a remote IP to scan: ")
source_ip = '10.0.0.190'

dport = 8000
sport = 9999
count = 0

print ""

while (count < 5):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((source_ip, sport))
        result = sock.connect_ex((target_ip, dport))
        data = sock.recv(1024)
        data = data.strip('\n')
        if "," in data:
            print "RX data =", data
            data = data.split(',')
            dport = int(data[0])
            sport = int(data[1])
            print "dport =", dport
            print "sport =", sport
            print ""
            sock.close()
            count +=1
        else:
            print "Flag is: ", data, "\n"
            break
    except KeyboardInterrupt:
        print "keyInterr\n"
        sys.exit()

    except socket.:(broken.......)
        print "host rejected on port {}:".format(port)

import time
import socket

for pings in range(1, 11):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Set timeout to 1s
    client_socket.settimeout(1.0)
    addr = ('', 12000)

    start = time.time()
    clock = time.time()

    #Message sent by Client
    message = b'Ping', pings, clock

    client_socket.sendto(str(message), addr)
    try:
        data, server = client_socket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print '\nPing:', pings, '\nRound Trip Time:', elapsed, 'seconds'
        print 'Server Response:',data

    except socket.timeout:
        print '\nPING:', pings, '\nREQUEST TIMED OUT'

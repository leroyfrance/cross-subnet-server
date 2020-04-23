import socket
import struct
import sys

multicast_group = '224.0.0.1'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive/respond loop
while True:

    print('\nwaiting to receive message', file=sys.stderr)
    data, address = sock.recvfrom(1024)
    
    print('received %s bytes from %s' % (len(data.decode()), address), file=sys.stderr)
    print(data.decode(), file=sys.stderr)

    print('sending acknowledgement to', address, file=sys.stderr)
    sock.sendto(b'ack', address)





import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_host = socket.gethostname()
udp_port = 12345

#msg = 'hello'
play = True

while play:
    msg = input('player 1 enter your choice: rock/paper/scissors ')
    msg = msg
    sock.sendto(msg.encode(),(udp_host,udp_port))

    encodedModified, serverAddress = sock.recvfrom(1024)
    print(encodedModified.decode())

    play = bool(int(input('would you like to play again? (0/1)')))

sock.close()
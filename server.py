from email import message
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_host = socket.gethostname()
udp_port = 12345


sock.bind((udp_host, udp_port))

while True:
    m, addr = sock.recvfrom(1024)
    m = str(m.decode())
    #print(m)

    msg = 'lalalalala'
    turn = input('player 2 enter your choice: rock/paper/scissor ')

    moves = ['rock','paper','scissor']
    if m in moves and turn in moves:
        if m==turn:
            msg = 'tie'
        elif m==moves[0] and turn==moves[1]:
            msg = 'player 2 wins'
        elif m==moves[0] and turn==moves[2]:
            msg = 'player 1 wins'
        elif m==moves[1] and turn==moves[0]:
            msg = 'player 1 wins'
        elif m==moves[1] and turn==moves[2]:
            msg = 'player 2 wins'
        elif m==moves[2] and turn==moves[0]:
            msg = 'player 1 wins'
        elif m==moves[2] and turn==moves[1]:
            msg = 'player 1 wins'
    else:
        msg = 'invalid input'
    
    print(msg)

    sock.sendto(msg.encode(), addr)

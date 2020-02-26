import socket

s = socket.socket()

s.connect(('final.ctf.bitx.tw', 30003))

recv_text = str(s.recv(4096), 'utf8')

print(recv_text)
exec(input('????????????????'))

s.sendall(bytes('101010100110', 'utf8'))

recv_text = str(s.recv(4096), 'utf8')

print(recv_text)

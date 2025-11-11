import socket



UDP_IP = "127.0.0.1"
UDP_PORT = 5005

msg = input('Escreva uma msg para o servidor: ')
MESSAGE = msg.encode(encoding="utf-8")  # representation in byte
# MESSAGE = b"Hello, World paulo!Tudo Bem!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

# Internet socket.AF_INET
# UDP socket.SOCK_DGRAM
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

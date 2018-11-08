import socket 
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 1234))
s.listen(1)
while True:
    print(s.accept()[1])
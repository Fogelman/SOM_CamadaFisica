import socket 
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 3333))

string="dudaduda"
b= [elem.encode("hex") for elem in string]
my_bytes = bytearray(b)

s.send(my_bytes)

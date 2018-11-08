import socket 
host= "localhost"
port=3333
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(("localhost", 3333))
dest= (host,port)
s.connect(dest)



# string="dudadbnvuda"
# my_bytes = bytearray(string)
# print(my_bytes)
msg= raw_input()

while True:
    mensagem = raw_input("coloca o seu texto aqui: ")
    print(mensagem)
    my_bytes = bytearray(str(mensagem))
    # print(my_bytes)
    s.sendto(my_bytes, dest)

s.close()

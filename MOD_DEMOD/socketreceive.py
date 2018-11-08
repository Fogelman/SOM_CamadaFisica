import socket 

host= "localhost"
port=1234
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig= (host,port)
s.bind(orig)
s.listen(1)
mensagem =[]
while True:
	con, cliente = s.accept()
	while True:
		msg = con.recv(1024)
		print(msg)
		mensagem.add(msg)
		if not msg: break
		print(cliente, mensagem)
	print("finalizando conexao do cliente", cliente)
	con.close()
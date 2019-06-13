import socket
conn = socket.socket()
addr = input('Введите адрес сервера ')
conn.connect((addr,7777))
print(conn.recv(1024).decode())

b = input('Введите матрицу в виде "[1 2; 3 4]" ')
conn.send(b.encode())
print(conn.recv(65565).decode())
conn.close()


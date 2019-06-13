import socket
sock = socket.socket()
sock.bind(('',7777))
sock.listen(1)
print('Ожидание подключения..')
conn, adr = sock.accept()
print('Подключен'+str(adr))
text = 'Отправьте матрицу'
conn.send(text.encode())
text = conn.recv(65565).decode()
lst = list(map(lambda x: x.strip().split(' '),text[1:-1].split(';')))
det = int(lst[0][0])*int(lst[1][1])-int(lst[0][1])*int(lst[1][0])
text = '[ '+str(int(lst[0][0])*det) + ' ' + str(int(lst[0][1])*det) + '; ' + str(int(lst[1][0])*det) + ' ' + str(int(lst[1][1])*det) + ' ]'
conn.send(text.encode())

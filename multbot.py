import socketserver

class BotHandler(socketserver.BaseRequestHandler):
	def handle(self):
		f = open('wget.py', 'r')
		self.data = self.request.recv(1024).strip()  # содержит данные из запроса
		print("Bot with IP {} ".format(self.client_address[0]))
		print('wrote:', self.data)  # отображает то, что отправил клиент
		self.request.sendall(self.data.upper())  # отправляет клиенту всю переданную ему информацию.

if __name__ == "__main__":   # позволяет проверять работает ли программа напрямую, либо она импортируется в другой модуль
	HOST, PORT = '', 8000
	tcpServer = socketserver.TCPServer((HOST, PORT), BotHandler)
	try:
		tcpServer.serve_forever()
	except:
		print("There was an error")
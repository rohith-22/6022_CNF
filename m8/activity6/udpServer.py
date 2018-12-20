import socket

def main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))

	print("Server Started")
	while True:
		data, addr = s.recvfrom(1024)
		print("Message from: " + str(addr))
		print("from connect user: " + str(data.decode()))
		data = str(data.decode()).upper()
		print("sending: " + str(data))
		s.sendto(data.encode(), addr)
	s.close()

if __name__ == '__main__':
	main()

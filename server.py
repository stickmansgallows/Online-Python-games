#!/usr/apps/bin/python
import asyncore
import socket
import time

serverHost = 'localhost'
serverPort = 50007

"""
Code Table:
All received data will begin with a letter to determine the use
2nd and 3rd characters will be the playerid given to the client at first log in
p: ping; 'p##'
c: connect 'cNAME'
d: disconnect 'd##'
r: reconnect 'rNAME'
s: say 's##STUFF'
"%02d"%num
"""

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(1024)
        if data:
    	if data[0] == 'p':
            		self.send(str(masterlist.unloadBuffer(int(data[1:3]))))
			masterlist.checkin(int(data[1:3]))
		elif data[0] == 'c':
			self.send("%02d" % masterlist.addPlayer(data[1:])) #Be sure to pad the zeroes
		elif data[0] == 'd':
			masterlist.diePlayer(int(data[1:3]))
		elif data[0] == 's':
			self.send(masterlist.sayPlayer(int(data[3:])))

class EchoServer(asyncore.dispatcher):
	def __init__(self, host, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind((host, port))
		self.listen(5)

	def handle_accept(self):
        	pair = self.accept()
        	if pair is None:
        		pass
        	else:
			sock, addr = pair
			print 'Incoming connection from %s' % repr(addr)
			handler = EchoHandler(sock)


class Playlist():
	def __init__(self):
		self.name = []
		#self.address = []
		self.pingtime = []
		self.active = []
		self.butter = []
	def addPlayer(self,name):
		try:
			i = self.name.index(name):
		except ValueError:			
			self.name.append(name)
			#self.address.append(address)
			self.pingtime.append(time.ctime(time.time()))
			self.butter.append([])
			self.active.append(True)
			return len(self.name)-1
		else:
			return i
	def diePlayer(self,i):
		self.active[i]=False
		#i = self.address.index(address)
		#self.name.pop(i)
		#self.address.pop(i)
		#self.pingtime.pop(i)
	def checkin(self,i):
		self.pingtime[i]=time.ctime(time.time())
	def checkTime(self):
		t = time.ctime(time.time())
		for i in range(len(self.name)):
			if t - self.pingtime[i] > 10: #Obviously needs real maths here
				self.diePlayer(i)
	def sayPlayer(self,m):
		for j in range(len(self.name)):
			self.butter[j].append(m)
	def unloadBuffer(self,i):
		if len(self.butter[i]) > 0:
			return self.butter[i].pop(0)
		else:
			return ''

if __name__ == '__main__':
	masterlist = Playlist()
	server = EchoServer(serverHost, serverPort)
	asyncore.loop()

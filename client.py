#!/usr/apps/bin/python
#############################################################
# Client side: use sockets to send data to the server, and 
# print server's reply to each message line; 'localhost' 
# means that the server is running on the same machine as 
# the client, which lets us test client and server on one 
# machine;  to test over the net, run server on a remote 
# machine, set serverHost to machine's domain name or IP addr;
#############################################################
 
import sys
from socket import *              # portable socket interface plus constants
from Tkinter import *

#serverHost = 'localhost'          # server name, or: 'starship.python.net'
#serverPort = 50007                # non-reserved port used by the server

class MessWin():
    def __init__(self, message, master):
		self.window = Toplevel(master)
		self.window.title(str(message))
		Label(self.window, text=str(message)).pack()

class ConWin():
	def __init__(self, master):
		self.window = Toplevel(master)
		self.master = master
		self.window.title("Connect to Server")
		self.ladd='localhost'
		self.lport=50007
		self.serverHost = Entry(self.window, textvariable=self.ladd)
		self.serverPort = Entry(self.window, textvariable=self.lport)
		self.serverHost.insert(0,'localhost')
		self.serverPort.insert(0,50007)
		self.serverHost.pack()
		self.serverPort.pack()
		Button(self.window, text="Connect", command=self.connect).pack()
		
	def connect(self):
		self.ladd = self.serverHost.get()
		self.lport = int(self.serverPort.get())
		message = ['Hello network world']           # text to send to server
		sockobj = socket(AF_INET, SOCK_STREAM)      # make a TCP/IP socket object
		sockobj.connect((self.ladd, self.lport))   # connect to serve and port
		for line in message:
		    sockobj.send(line)                      # send line to server over socket
		    data = sockobj.recv(1024)               # receive from server: up to 1k
		
		    #print 'Client received:', `data`
 		
		
		#MessWin(data,self.master)
		sockobj.close()                             # close to send eof to server
		self.window.destroy()
		LobbyWin(self.master, self.ladd,self.lport)
		
class LobbyWin():
	def __init__(self, master,ladd,lport):
		self.sadd=ladd
		self.sport=lport
		self.window = Toplevel(master)
		self.master = master
		self.chat = Text(self.window, height=40, width=80)
		self.enter = Entry(self.window,width=60)
		self.chat.pack()
		self.enter.pack(side=LEFT)
		self.send = Button(self.window,text="Send",command=self.sendWords).pack(side=RIGHT)
		
		message = ['This is a beautiful day']
		for i in range(10):
			sockobj = socket(AF_INET, SOCK_STREAM)      # make a TCP/IP socket object
			sockobj.connect((self.sadd, self.sport))   # connect to serve and port
			for line in message:
		    		sockobj.send(line)                      # send line to server over socket
		    		data = sockobj.recv(1024)               # receive from server: up to 1k
				self.chat.insert(END, data+"\n")
				self.chat.update()
			sockobj.close()
		sys.exit(0)
	def sendWords(self):
		print self.enter.get()
		self.enter.delete(0,END)

if __name__ == "__main__":	#Main
    root = Tk()
    root.wm_withdraw()
    ConWin(root)
    root.mainloop()

#!/usr/apps/bin/python
 
import sys
from socket import *              # portable socket interface plus constants
from Tkinter import *
import time

serverHost = 'localhost'          # server name, or: 'starship.python.net'
serverPort = 50007               # non-reserved port used by the server
pid = '00'

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
		self.ladd=serverHost
		self.lport=serverPort
		self.serverHost = Entry(self.window, textvariable=self.ladd)
		self.serverPort = Entry(self.window, textvariable=self.lport)
		self.serverHost.insert(0,serverHost)
		self.serverPort.insert(0,serverPort)
		self.serverHost.pack()
		self.serverPort.pack()
		Button(self.window, text="Connect", command=self.connect).pack()
		
	def connect(self):
		global serverHost 
		serverHost = self.serverHost.get()
		global serverPort 
		serverPort = int(self.serverPort.get())
		global pid
		message="cStickman"
		pid = sendReceive(message)
		self.window.destroy()
		LobbyWin(self.master)
		
class LobbyWin():
	def __init__(self, master):
		self.window = Toplevel(master)
		self.master = master
		self.chat = Text(self.window, height=40, width=80)
		self.enter = Entry(self.window,width=60)
		self.chat.pack()
		self.enter.pack(side=LEFT)
		self.send = Button(self.window,text="Send",command=self.sendWords).pack(side=RIGHT)
		
		for i in range(20):
			message = 'p'+pid
			print sendReceive(message)
		
		sys.exit(0)
	def sendWords(self):
		print self.enter.get()
		self.enter.delete(0,END)
		
def sendReceive(message):
	sockobj = socket(AF_INET, SOCK_STREAM)      # make a TCP/IP socket object
	sockobj.connect((serverHost, serverPort))   # connect to serve and port
	sockobj.send(message)                      # send line to server over socket
	data = sockobj.recv(1024)               # receive from server: up to 1k
	sockobj.close()
	print "Send: "+message+"   Receive: "+data
	return data
	

if __name__ == "__main__":	#Main
    root = Tk()
    root.wm_withdraw()
    ConWin(root)
    root.mainloop()

#!/usr/apps/bin/python

import SocketServer, time               # get socket server, handler objects
myHost = ''                             # server machine, '' means local host
myPort = 50007                          # listen on a non-reserved port number
def now(): 
    return time.ctime(time.time())
 
class MyClientHandler(SocketServer.BaseRequestHandler):
    def handle(self):                           # on each client connect
        print self.client_address, now()        # show this client's addr
        time.sleep(4)                           # simulate blocking activity
        while 1:                                # self.request is client socket
            data = self.request.recv(1024)      # read, write a client socket
            if not data: break
            self.request.send('Echo=>%s at %s' % (data, now()))
        self.request.close() 
 
# make a threaded server, listen/handle clients forever
myaddr = (myHost, myPort)
server = SocketServer.ThreadingTCPServer(myaddr, MyClientHandler)
server.serve_forever() 

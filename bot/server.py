import socketserver
import os

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print ("{} wrote:"+format(self.client_address))
        print (self.data)
        resp = str(self.data)


        if 'furhat'  in resp:
            resp = resp.split(',')
            f = open("furhat.txt", "w")
            f.write(resp[1])
            f.close()
            f = open("resp.txt", "r")
            res = str(f.read())
            print(res)
            if res == "":
                a = "there is no message"
                self.request.sendall(a.encode())
            else:
                self.request.sendall(res.encode())

        if 'test' in resp:
            f = open("resp.txt", "r")
            res = str(f.read())
            print(res)
            if res == "":
                a = "there is no message"
                self.request.sendall(a.encode())
            else:
                f = open("resp.txt", "w")
                f.write("")
                f.close()
                self.request.sendall(res.encode())

        #if 'asr' in resp:
            #open and read the file after the appending:
            #f = open("furhat.txt", "r")

            #res = str(f.read())
            #print(res)
            #f = open("furhat.txt", "w")
            #f.write("")
            #f.close()
            #self.request.sendall(res.encode())

        #if 'from the bot' in resp:
        #    print(resp)
        #    resp = (resp.decode('utf-8'))
        #    resp = resp.split('+')
        #    print(resp[1])
        #    f = open("resp.txt", "w")
        #    f.write(resp[1])
        #    f.close()
        #    self.request.sendall(resp[1].encode())




if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

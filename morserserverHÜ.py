#!/usr/bin/env python3
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    #morse code table
    code = {"1":".----",
        "2":"..---",
        "3":"...--",
        "4":"....-",
	    "5":".....",
	    "6":"-....",
	    "7":"--...",
	    "8":"---..",
	    "9":"----.",
	    "0":"-----"} #continue until "0"
        
    def morse(zeichen, led):
        if zeichen not in code:
            print("Nicht vorhanden")
            return
        print(code[zeichen])
        for n in code[zeichen]:
            if n==".":
                ed.blink(TDOT,TDOT,1,False)
                print(".")
            else:
                led.blink(3*TDOT,TDOT,1,False)
                print("-")
    
    
    while True:
        nachricht = input("zahl: ")
        if nachricht == "#":
            print("Auf Wiedersehen")
            break
        for z in nachricht:
            print(z)
            morse(z, led)
            sleep(2*TDOT)

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

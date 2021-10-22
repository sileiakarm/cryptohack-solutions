import sys
import binascii
import telnetlib
import base64
import codecs
import json


# defining functions
#decoding function based on type
def decode(encodedType, encodedContent):
    
    if encodedType == 'base64':
        return base64.b64decode(encodedContent).decode('utf-8')
    elif encodedType == 'hex':
        return binascii.unhexlify(encodedContent).decode('utf-8')
    elif encodedType == 'bigint':
        return binascii.unhexlify(encodedContent.replace('0x', '')).decode('utf-8')
    elif encodedType == 'rot13':
        return codecs.encode(encodedContent, 'rot_13')
    elif encodedType == 'utf-8':
        s = ""
        for c in encodedContent:
            s += chr(c)
        return s

# connect to server
HOST = "socket.cryptohack.org"
PORT = 13377

telnet = telnetlib.Telnet(HOST, PORT)

def readline():
        return telnet.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    telnet.write(request)

#program start 

while True:
    
    received = json_recv()
    
    # if the flag turns up, print and exit program
    if "flag" in received:
        print("FLAG: %s" % received["flag"])
        sys.exit(0)

    # decode the received content based on it's type
    to_send = {
        "decoded": decode(received["type"], received["encoded"])
    }

    json_send(to_send)

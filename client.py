import socket
from server import blt_address

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect((blt_address,4))

try:
    while True :
        message = input('Enter Message :')
        client.send(message.encode("utf-8"))
        data = client.recv(1024)
        if not data : break
        
        print(f"message : {data.decode('utf-8')}")
except OSError as e:
    print(e)    
    
client.close()
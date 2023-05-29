import socket

# get clients blutooth address 
# How to get client address
# step :
# 1. go to device manager
# 2. bluetooth -> right click on selected bluetooth device and open up property -> advance option -> get the address
blt_address = ""

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind((blt_address,4))
server.listen(1)

client, addr = server.accept()

try:
    while True :
        data = client.recv(1024)    
        if not data : break
        
        print(f"Message : {data.decode('utf-8')}")
        message = input('Enter message :')
        client.send(message.encode('utf-8'))
except OSError as e: print(e)

client.close()
server.close()
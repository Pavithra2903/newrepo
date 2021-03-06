import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 12345                   # Reserve a port for your service.

s.connect((host, port))
s.send(b"Hello server!")

with open('received_file', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s' %data)
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully received the file')
s.close()
#print the result
print('connection closed')
import socket
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:    
 
    client_connection, client_address = server_socket.accept()

    
    request = client_connection.recv(1024).decode()
    print(request)
    
    headers = request.split('\n')
    route = headers[0].split()[1]
    filename = ""
   
    if route == '/':
        filename = 'index.html'
    elif route == "/detail_elaina" :
        filename = "detail_elaina.html"
    elif route == "/oneokcat" :
        filename = "oneokcat.html"
    elif route == "messi_facts":
        filename = "messi_facts.html"
    try:
        fin = open(filename)
        content = fin.read()
        fin.close()

        response = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:

        response = 'HTTP/1.0 404 NOT FOUND\n\n404 NOT FOUND'
    client_connection.sendall(response.encode())
    client_connection.close()



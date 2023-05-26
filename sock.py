import socket #import package socket
SERVER_HOST = '127.0.0.1' #server host untuk dibuka di web browser
SERVER_PORT = 8000 #port 8000 untuk bisa akses di web browser nya


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
    route = headers[0].split()[1] #ambil route nya dari request
    type_req = headers[9].split()[1].split()[0].split() #ambil type_req nya apakah html atau bukan
    get_type = type_req[0][0:9] #ambil hanya text/html nya aja
    filename = "" # ini untuk nanti dimasukkan di pas buka web browser nya.
   
    if route == '/':  #check apabila pas di buka route nya adalah / maka tampilkan index.html
        filename = 'index.html'
    elif route == "/detail_elaina" : #check apabila pas di buka route nya detail_elaina maka tampilkan detail_elaina.html
        filename = "detail_elaina.html"
    elif route == "/oneokcat" : #check apabila pas di buka  route one ok cat atau bukan kalo iya maka tampilkan oneokcat.html
        filename = "oneokcat.html"
    elif route == "/messi_facts": #check apabila pas di buka route nya messi facts atau bukan kalau iya maka tampilkan messifacts.html
        filename = "messi_facts.html"
    try:
        fin = open(filename) #buka file sesuai dengan file name dari client membuka route mana di web browser
        content = fin.read() # baca cisi dari file name nya
        fin.close() #setelah membaca baru di close

        response = 'HTTP/1.0 200 OK\n\n' + content #untuk check response nya kalau responenya 200 maka tampilkan content nya 
        req = response.split() #ini untuk ngambil status code nya dari response
        print("======================================")
        print("Client Request")
        if(req[1] == "200") : # ini untuk ngambil status code nya apakah 200 atau bukan kalo iya tampilkan type nya apa yang dikeluarin di response.
            print(get_type)

        
      
        print("======================================")

    except FileNotFoundError:

        response = 'HTTP/1.0 404 NOT FOUND\n\n404 NOT FOUND' #kalo response nya 404 not found berarti tidak ada file atau tidak termasuk dalam persyaratan route diatas
        req = response.split() #check status codenya.
        if(req[1] == "400") : # apabila status kode nya 400 maka tampilkan not found
            print("Not found ")
    client_connection.sendall(response.encode()) # kirim semua ke response yang sudah di encode.
    client_connection.close() # kalo sudah maka akan di close.



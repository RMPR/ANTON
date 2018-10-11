import BaseHTTPServer


HOST_NAME = "ip"  # Change this
PORT_NUMBER = 80

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()


    def do_POST(self):
        
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(post_data)
        self._set_headers()


if __name__ == '__main__':
    
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print('Server started on port 80...')
    
    try:
        httpd.serve_forever()
        
        
    except KeyboardInterrupt:
        print('[+] Server is terminated')
        httpd.server_close()
        

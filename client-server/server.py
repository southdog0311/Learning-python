from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('request url:', self.path)
        if self.path == '/':
            self.send_response(200)
            self.send_header('info', 'index')
            self.end_headers()
            self.wfile.write(b'index')
        elif self.path == '/redirect':
            self.send_response(301)
            self.send_header('Location', 'https://google.com')
            self.end_headers()
        elif self.path == '/category':
            self.send_response(200)
            self.send_header('info', 'category')
            self.end_headers()
            self.wfile.write(b'category')
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

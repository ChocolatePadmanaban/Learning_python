#creating a local host server



from http.server import BaseHTTPRequestHandler,HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path =='./hello':
            self.send_response(200,"OK")
            self.send_header("Content-type","text/plain")
            self.end_headers()
            self.wfile.write(b"""
            <HTML>
            <HEAD>
            <TITLE>Hello</TITLE>
            </HEAD>
            <BODY>"Hello World"</BODY>
            </HTML>            
            """)
serv = HTTPServer(("",8080),HelloHandler)
serv.serve_forever()
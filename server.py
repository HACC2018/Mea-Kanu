from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO
import os
import base64
import chardet
import socket

def EncodeDecode(img):
    #Get the type of encoding the bytes are saved in from the chardet.detect call
    #chardet returns a dictonary
    #ex: {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
    encode_type = list(chardet.detect(img).values())
    
    if encode_type[0] == None:
        pass
    #once encoding is decode back into a string
    else:
        img = img.decode(encode_type[0])
        img = img.encode('utf-8')
    #encode once again in base64 to ensure all information is received as a base64 byte str
    
    img = base64.b64encode(img)

    return img

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        print(chardet.detect(body))
        
        print(type(body))
        body = EncodeDecode(body)
        decode = base64.b64decode(body)
        output_file = open("new_aloe.jpg", "wb")
        output_file.write(decode)
        output_file.close()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(b"Hello")
        
        
        #self.send_response(200, "Success")
        #self.end_headers()


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
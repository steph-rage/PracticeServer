from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		with open('input_questions.html', 'r') as html_file:
			self.wfile.write(bytes(html_file.read(), 'utf8'))
		return

	def do_POST(self):
		self.send_response(200)
		self.end_headers()
		with open('input_questions.html', 'r') as html_file:
			self.wfile.write(bytes(html_file.read(), 'utf8'))
		#Get the question sent via POST
		question = self.rfile.read(int(self.headers.get('content-length')))
		return


def run(server_class=HTTPServer, handler_class=Handler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()

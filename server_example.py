from http.server import HTTPServer, BaseHTTPRequestHandler



class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		if "?" in self.requestline:
			input_numbers = self.requestline.split('=')
			try:
				number_1 = int(input_numbers[1].split('&')[0])
			except ValueError:
				number_1 = 0
			try:
				number_2 = int(input_numbers[2].split(' ')[0])
			except ValueError:
				number_2 = 0
			my_sum = number_1 + number_2
			with open('results.html', 'r') as results_page:
				self.wfile.write(bytes(results_page.read().format(my_sum), 'utf8'))
		else:
			with open('example.html', 'r') as html_file:
				self.wfile.write(bytes(html_file.read(), 'utf8'))
		return



def run(server_class=HTTPServer, handler_class=Handler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()

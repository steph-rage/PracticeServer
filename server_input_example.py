from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse

questions = []
html_footer = "</body></html>"

class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		with open('input_questions.html', 'r') as html_file:
			html = html_file.read() 
			html += html_footer
			self.wfile.write(bytes(html, 'utf8'))
		return

	def do_POST(self):
		self.send_response(200)
		self.end_headers()
		#Get the question sent via POST:
		#get the correct length of the question from the headers, then read in from rfile
		#decode into utf8, parse using urllib, then split for just the question text
		new_question = parse.unquote_plus(self.rfile.read(int(self.headers.get('content-length'))).decode('utf8')).split('=')
		questions.append(new_question[1])
		with open('input_questions.html', 'r') as html_file:
			html = html_file.read()
			html += "<ol>"
			for question in questions:
				html += "<li>{}</li>".format(question)
			html += "</ol>"
			html += html_footer
			self.wfile.write(bytes(html, 'utf8'))
		return




def run(server_class=HTTPServer, handler_class=Handler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()

#!/usr/bin/python3

import webapp
import random

class aleatApp(webapp.webApp):
	
	def process(self, parsedRequest):
		num = random.randint(0,1000000)
		response = '<html><body><h1>Hola <a href="//localhost:1234/'+ str(num) + '">Dame Otra</a></h1></body></html>\r\n'
		return ("200 OK", response)

if __name__ == "__main__":
	MyWebApp = aleatApp("localhost", 1234)

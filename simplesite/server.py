import logging
import BaseHTTPServer
import SimpleHTTPServer

class Server(object):

  def __init__(self, path, port):
    self.path = path
    self.port = port

  def serve(self):
    try:
      server = BaseHTTPServer.HTTPServer(('', self.port), SimpleHTTPServer.SimpleHTTPRequestHandler)
      logging.info("Serving at port %s.", self.port)

      server.serve_forever()
    except KeyboardInterrupt as e:
      logging.info("Shutting down server.")
      server.socket.close()
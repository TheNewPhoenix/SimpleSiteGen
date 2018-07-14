import logging
import BaseHTTPServer
import SimpleHTTPServer

logger = logging.getLogger(__name__)

class Server(object):

  def __init__(self, path, port):
    self.path = path
    self.port = port

  def serve(self):
    try:
      server = BaseHTTPServer.HTTPServer(('', self.port), SimpleHTTPServer.SimpleHTTPRequestHandler)
      logger.info("Serving at port %s.", self.port)

      server.serve_forever()
    except KeyboardInterrupt:
      logger.info("Shutting down server.")
      server.socket.close()
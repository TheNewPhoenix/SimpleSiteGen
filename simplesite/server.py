import logging
import BaseHTTPServer
import SimpleHTTPServer
import webbrowser

logger = logging.getLogger(__name__)

class Server(object):

  def __init__(self, path, port, browser):
    self.path = path
    self.port = port
    self.browser = browser

  def serve(self):
    try:
      server = BaseHTTPServer.HTTPServer(('', self.port), SimpleHTTPServer.SimpleHTTPRequestHandler)
      
      logger.info("Serving at port %s.", self.port)
      
      if self.browser is True:
        logger.info("Opening in browser")
        webbrowser.open('http://127.0.0.1:%s' % self.port)
      
      server.serve_forever()

    except KeyboardInterrupt:
      logger.info("Shutting down server.")
      server.socket.close()
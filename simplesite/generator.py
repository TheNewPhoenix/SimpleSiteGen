import os
import shutil
import logging
import json

logger = logging.getLogger(__name__)

HTMLTEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>title</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width">

    <link rel="stylesheet" href="/css/main.css">
  </head>

  <body>
    <h1>TITLE</h1>
    <p>Welcome to your custom website</p>
    <script src="/js/main.js"></script>
  </body>

</html>
"""

class Generator(object):

  def __init__(self, path, title):
    self.path = path
    self.title = title

  def generate(self):
    create_path = os.path.join(self.path, self.title)
    
    static_path = os.path.join(create_path, 'static')
    pages_path = os.path.join(create_path, 'pages')
    folders = [
      pages_path,
      os.path.join(create_path, 'layouts'),
      os.path.join(static_path, 'css'),
      os.path.join(static_path, 'js'),
      os.path.join(static_path, 'img'),
      os.path.join(static_path, 'fonts'),
    ]

    for folder in folders:
      try:
        os.makedirs(folder, 0755)
      except OSError:
        logger.error("Failed to create dir: %s", folder)

    with open(os.path.join(pages_path, 'index.html'), 'w+') as index:
      index.write(HTMLTEMPLATE)

    self.create_config(create_path)
    
    logger.info("Created website: %s in: %s", self.title, create_path)

  def create_config(self, path):
    data = {}
    data['URL'] = 'http://example.com/'
    data['title'] = self.title

    config_file = os.path.join(path, 'config.json')
    with open(config_file, 'w+') as outfile:
      json.dump(data, outfile)
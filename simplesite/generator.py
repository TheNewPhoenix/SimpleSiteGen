import os
import shutil

class Generator(object):

  def __init__(self, path, title):
    self.path = path
    self.title = title
    self.folders = []
    self.files = []

  def generate(self):
    modulePath = os.path.dirname(__file__)
    templatePath = os.path.join(modulePath, 'template')
    createPath = os.path.join(self.path, self.title)

    print "Generating a website titled {}".format(self.title)
    print "Moving files from {} to {}".format(templatePath, createPath)
    shutil.copytree(templatePath, createPath)
    

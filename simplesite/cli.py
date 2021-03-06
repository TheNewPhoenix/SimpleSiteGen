import os
import argparse

class SimpleSite(object):
  
  def __init__(self):
    self.Generator = None
    self.Server = None

  def setup(self):
    from simplesite.generator import Generator
    from simplesite.server import Server
    self.Generator = Generator
    self.Server = Server
  
  def create(self, path, title):
    generator = self.Generator(path, title)
    generator.generate()
  
  def serve(self, path, port, browser):
    server = self.Server(path, port, browser)
    server.serve()

def parse_args(site):
  parser = argparse.ArgumentParser(description="Simple static website generator and server.")

  subparsers = parser.add_subparsers(title='subcommands', description='Valid subcommands', 
                                     help='Select a command to run.', dest='command')

  subparsers.required = True

  parser_create = subparsers.add_parser('create', help='Creates a new project.')
  parser_create.add_argument('title', help='The title of your website.')
  parser_create.set_defaults(target=site.create)

  parser_serve = subparsers.add_parser('serve', help='Serves the project')
  parser_serve.add_argument('-p', '--port', default=8000, type=int, help='Port that the website is served from.')
  parser_serve.add_argument('-b', '--browser', action='store_true', help='Whether to open in browser.')
  parser_serve.set_defaults(target=site.serve)
  
  commands = [parser_create, parser_serve]
  for command in commands:
    command.add_argument('-d', '--path', default=os.getcwd(), help='The path of the current project.')
    command.add_argument('-v', '--verbose', action='store_true', help='Be more verbose.')
    command.add_argument('-q', '--quiet', action='store_true', help='Be quieter.')

  args = parser.parse_args()

  return args

def main():
  site = SimpleSite()
  args = parse_args(site)

  site.setup()

  import simplesite.log as log
  log.init(args.verbose, args.quiet)

  kwargs = dict((k, v) for k, v in vars(args).items() if k not in ['command', 'target', 'verbose', 'quiet'])
  args.target(**kwargs)

if __name__ == "__main__":
  main()
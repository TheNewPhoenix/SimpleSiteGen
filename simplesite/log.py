import os
import logging

def init(verbose, quiet):

  logger = logging.getLogger()
  handler = logging.StreamHandler()

  log_level = logging.INFO

  if quiet:
    log_level = logging.WARNING
  elif verbose:
    log_level = logging.DEBUG
  else:
    log_level = logging.INFO

  logger.setLevel(log_level)

  for h in logger.handlers:
    logger.removeHandler(h)

  logger.addHandler(handler)
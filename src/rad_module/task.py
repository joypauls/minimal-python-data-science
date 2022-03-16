import os
import time
import logging

logger = logging.getLogger(__name__)


class Task:
  """Sample task runner"""
  def __init__(self):
    self.name = os.getenv("EXAMPLE_JOB_NAME_VARIABLE", "default")

  def execute(self):
    logger.info("executing task: {}".format(self.name))
    time.sleep(1)

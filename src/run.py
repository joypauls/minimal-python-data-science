import logging
from datetime import datetime, timedelta
from rad_module.task import Task

# setup logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


# main function that executes when script runs
def main():
  logger.info("START")
  t0 = datetime.now()

  # do the thing
  task = Task()
  task.execute()

  t1 = datetime.now()
  logger.info("time elapsed (seconds): {}".format((t1 - t0).total_seconds()))
  logger.info("END")

if __name__ == "__main__":
  main()
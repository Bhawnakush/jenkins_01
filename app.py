import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

logging.info("Container is running...")

while True:
    logging.info("App is alive")
    time.sleep(10)

import argparse
from cron_parser import expand_cron_expression
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('cron_parser.log')
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)







parser = argparse.ArgumentParser(description='Expand cron expression')
parser.add_argument('cron_expression', type=str, 
                    help='The cron expression to expand')

args = parser.parse_args()

try:
    expanded_fields = expand_cron_expression(args.cron_expression)
except ValueError as e:
    logger.error(f"Invalid expression: {e}")
    exit(1)

logger.info("Expanded Expression:")
print("Expanded Expression:")
for field, values in zip(["minute", "hour", "day of month", "month", "day of week", "command"], expanded_fields):
    print(f"{field:14} {values}")
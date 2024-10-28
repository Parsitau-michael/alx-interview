#!/usr/bin/python3
"""
This script reads log lines from standard input (stdin) and calculates metrics
based on the provided log format. It tracks the total file size and counts of
HTTP status codes. Metrics are printed every 10 lines and when interrupted
with CTRL + C.

Expected log line format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

For example:
192.168.1.1 - [2024-10-28 10:00:00] "GET /projects/260 HTTP/1.1" 200 1234

Functionality:
- Tracks total file size.
- Counts occurrences of each HTTP status code.
- Prints metrics every 10 lines and on keyboard interruption (CTRL + C).
"""


import sys
import re
import signal

# pattern definition
regex = (
    r'^(?P<ip>\S+) - \[(?P<dt>.*?)\] "GET /projects/260 HTTP/1.1" '
    r'(?P<sc>\d{3}) (?P<fs>\d+)$'
    )

# Variable initializations
line_count = 0
total_file_size = 0
status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
status_code_counts = {key: 0 for key in status_codes}


def print_metrics(signal_number=None, frame=None):
    """
    Prints the current metrics including total file size and counts of
    HTTP status codes.

    Args:
        signal_number (int): The signal number (unused in function).
        frame (frame object): The current stack frame (unused in function).

    Metrics:
    - Total file size: Sum of file sizes from all processed log lines.
    - Status code counts: A count of each HTTP status code that appears
      in the logs.
      Only status codes 200, 301, 400, 401, 403, 404, 405, and 500 are counted
      and printed in ascending order.
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


# Register signal handler
signal.signal(signal.SIGINT, print_metrics)

# processing each line from sys.stdin
try:
    for line in sys.stdin:
        line = line.strip()
        match = re.match(regex, line)

        # Only process lines that match
        if match:
            line_count += 1
            total_file_size += int(match.group('fs'))
            status_code = match.group('sc')
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            # Print metrics after every 10 lines
            if line_count % 10 == 0:
                print_metrics()
except KeyboardInterrupt:
    print_metrics()
    raise

# Print any remaining metrics
print_metrics()

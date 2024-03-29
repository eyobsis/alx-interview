#!/usr/bin/python3
"""Log Parsing Script

This script reads log entries from standard input (stdin), parses them according to a specific format,
and computes metrics based on the parsed data.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys
import signal
import re

total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """Prints the accumulated statistics."""
    print("File size:", total_file_size)
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(code, ":", status_code_count[code])

def signal_handler(sig, frame):
    """Signal handler for Ctrl+C."""
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

log_pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

for line in sys.stdin:
    line_count += 1
    match = log_pattern.match(line.strip())
    if match:
        file_size = int(match.group(4))
        total_file_size += file_size
        status_code = int(match.group(3))
        if status_code in status_code_count:
            status_code_count[status_code] += 1
    if line_count == 10:
        print_statistics()
        line_count = 0

print_statistics()


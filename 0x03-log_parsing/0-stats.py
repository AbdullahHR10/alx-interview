#!/usr/bin/python3
""" Moudle that contains a python script. """

import sys
import re
from collections import defaultdict


def process_logs():
    """ Reads log entries from standard input,
    processes valid lines based on the specified format,
    and computes metrics. """
    total_file_size = 0
    status_code_count = defaultdict(int)
    line_count = 0
    log_pattern = re.compile(r'^(?P<ip>[0-9\.]+) - \[(?P<date>[^\]]+\]) "(?P<method>GET) (?P<path>/projects/\d+) HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)$')
    try:
        for line in sys.stdin:
            line = line.strip()
            match = log_pattern.match(line)
            if match:
                status_code = match.group('status')
                file_size = int(match.group('size'))
                total_file_size += file_size
                status_code_count[status_code] += 1
                line_count += 1
            if line_count % 10 == 0:
                print_metrics(total_file_size, status_code_count)
    except KeyboardInterrupt:
        print_metrics(total_file_size, status_code_count)

def print_metrics(total_file_size, status_code_count):
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_count.keys()):
        print(f"{status_code}: {status_code_count[status_code]}")


if __name__ == "__main__":
    process_logs()

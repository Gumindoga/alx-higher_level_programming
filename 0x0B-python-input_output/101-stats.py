#!/usr/bin/python3
"""
This module reads stdin line by line and computes metrics.
"""

import sys


def compute_metrics():
    """
    Compute metrics from stdin.

    This function reads from stdin line by line, splits each line into words,
    and extracts the status code and file size from the end of each line.
    It keeps a running total of the file size and counts of each status code.
    Every 10 lines, it prints the total file size & counts of each status code.
    It also handles a KeyboardInterrupt (CTRL + C) gracefully, printing the
    metrics before exiting.
    """
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    file_size = 0
    try:
        for i, line in enumerate(sys.stdin, 1):
            split_line = line.split()
            if len(split_line) < 2 or not split_line[-2].isdigit():
                continue
            status_code = int(split_line[-2])
            file_size += int(split_line[-1])
            if status_code in status_codes:
                status_codes[status_code] += 1
            if i % 10 == 0:
                print("File size: {}".format(file_size))
                for code in sorted(status_codes.keys()):
                    if status_codes[code] > 0:
                        print("{}: {}".format(code, status_codes[code]))
    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {}".format(file_size))
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    compute_metrics()

#!/usr/bin/python3
"""
Log parsing
"""

import sys


if __name__ == '__main__':

    file_size_total, line_count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    http_status_codes = codes
    http_status_stats = {k: 0 for k in http_status_codes}

    def print_statistics(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(file_size))
        for code, count in sorted(stats.items()):
            if count:
                print("{}: {}".format(code, count))

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in http_status_stats:
                    http_status_stats[status_code] += 1
            except IndexError:
                pass
            try:
                file_size_total += int(data[-1])
            except (IndexError, ValueError):
                pass
            if line_count % 10 == 0:
                print_statistics(http_status_stats, file_size_total)
        print_statistics(http_status_stats, file_size_total)
    except KeyboardInterrupt:
        print_statistics(http_status_stats, file_size_total)
        raise

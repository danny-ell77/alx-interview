#!/usr/bin/python3
"""This module prints out HTTP Request Stats"""


def print_stats(stats):
    """Prints to stdout the Stats"""
    print(f"File size: {stats.get('file_size')}", flush=True)

    status_codes = sorted(list(stats.keys())[1:])
    for key in status_codes:
        if value := stats.get(key):
            print(f"{key}: {value}", flush=True)


def main():
    """Main entfry point"""
    stats = {
        "file_size": 0,
    }
    while True:
        for _ in range(10):
            try:
                line = input()
                status_code, file_size = line.split(" ")[-2:]
                status_code = int(status_code)
                file_size = int(file_size)

                stats["file_size"] += file_size
                stats[status_code] = stats.get(status_code, 0) + 1
            except ValueError:
                continue
            except KeyboardInterrupt:
                print_stats(stats)
                raise
        print_stats(stats)


if __name__ == "__main__":
    main()

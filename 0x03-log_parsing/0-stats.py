#!/usr/bin/python3
"""This module prints out HTTP Request Stats"""


def print_stats(stats):
    """Prints to stdout the Stats"""
    print(f"File size: {stats['file_size']}", flush=True)
    for key, value in stats.items():
        if not key == "file_size" and value > 0:
            print(f"{key}: {value}", flush=True)


def main():
    """Main entfry point"""
    while True:
        stats = {
            "file_size": 0,
        }
        for _ in range(10):
            try:
                line = input()
                print(line)
                status_code, file_size = line.split(" ")[-2:]
                status_code = int(status_code)
                file_size = int(file_size)

                stats["file_size"] += file_size
                stats[status_code] = stats.get(status_code, 0) + 1
            except ValueError:
                continue
            except KeyboardInterrupt:
                print_stats(stats)
        print_stats(stats)


if __name__ == "__main__":
    main()

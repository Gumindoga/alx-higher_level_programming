#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc = sys.argv

    if len(argc) == 1:
        print("0 arguments.")
    elif len(argc) == 2:
        print("1 argument:")
    elif len(argc) > 2:
        print(f"{len(argc) - 1} arguments:")

    if len(argc) > 1:
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"{i}: {arg}")

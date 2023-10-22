#!/usr/bin/python3
print("".join(chr(i).format() for i in range(97, 123) if chr(i) not in ['q', 'e']), end="")

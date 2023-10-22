#!/usr/bin/python3
print("".join([chr(122 - i).format() if i % 2 == 0
               else chr(90 - i).format() for i in range(26)]), end="")

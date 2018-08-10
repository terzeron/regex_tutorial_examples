#!/usr/bin/env python
import sys
import re

def main():
    str = "red apple green blue apple"
    matches = re.findall(r'(red|green|blue) (\w+)', str)
    for m in matches:
        print("%s -> %s" % (m[0], m[1]))

        
if __name__ == "__main__":
    sys.exit(main())

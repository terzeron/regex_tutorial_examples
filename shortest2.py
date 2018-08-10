#!/usr/bin/env python
import sys
import re

def main():
    str = 'Computer says "yes", Phone says "no"'
    m = re.search(r'"(.+)"', str)
    if m:
        print(m.group(1))

        
if __name__ == "__main__":
    sys.exit(main())

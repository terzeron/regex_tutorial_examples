#!/usr/bin/env python
import sys
import re

def main():
    str = "Age: 18"
    m = re.search(r'Age: (?P<age>\d+)', str)
    if m:
        print(m.group("age"))

        
if __name__ == "__main__":
    sys.exit(main())

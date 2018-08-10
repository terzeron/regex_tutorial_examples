#!/usr/bin/env python


import sys
import re


def main():
    with open('test.txt', 'r') as f:
        while True:
            line = f.readline()
            m = re.search(r'패턴', line)
            if m:    
                print(m.group(1))
                print(m.group(2))
        

if __name__ == "__main__":
    sys.exit(main())

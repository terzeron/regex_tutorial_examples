#!/usr/bin/env python


import sys
import re


def main():
    str = '대상 문자열'

    m = re.search(r'패턴', str)
    if m:    
        print(m.group(1))
        print(m.group(2))
        

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python


import sys
import re


def main():
    str = ''' <div class="row1">
    <p>hello</p>
    </div> '''

    m = re.search(r'<div class="(\w+)">\s*(.*)\s*</div>', str, re.M)
    if m:    
        print(m.group(1))
        print(m.group(2))
        

if __name__ == "__main__":
    sys.exit(main())

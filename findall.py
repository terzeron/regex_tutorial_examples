#!/usr/bin/env python
import sys
import re

def main():
    str = "He was carefully disguised but captured quickly by police."
    #m = re.findall(r'(\w+ly)', str) 
    m = re.findall(r'(\w+ly)\s+(\w+ed)', str)
    for group in m:
        print(group[0]) 


        
if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
import sys
for member in sys.argv[1:]:
    num = member.split(':')
    salary = int(num[1])
    print(salary)

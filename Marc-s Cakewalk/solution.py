#!/bin/python

import sys


n = int(raw_input().strip())
calories = map(int, raw_input().strip().split(' '))
calories.sort(reverse=True)
count=0
for i in range (n):
    count+= calories[i]*(2**i)
    
print count

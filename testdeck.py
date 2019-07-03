#!/bin/python3

import sys
import os
import re


# Complete the function below.

def  MergeStrings(strings):
    strings = re.sub(r'[A-Z]', '', strings)
    
    return ''.join(sorted(strings))

print(MergeStrings('ghghGh'))

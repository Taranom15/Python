#!/bin/python3

import math
import os
import random
import re
import sys


def timeInWords(h, m):   
    hour= ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']

    if m == 0 :
        text = hour[h-1] + " o\' clock"   
    elif  m == 1:
        text = "one minute past " + hour[h-1]    
    elif  m == 15:
        text = "quarter past " + hour[h-1]   
    elif m < 30 :
        text = hour[m-1] + " minutes past " + hour[h-1]
    elif  m == 30:
        text = "half past " + hour[h-1]     
    elif  m == 45:
        text = "quarter to " + hour[h]   
    elif  m == 59:
        text = "one minute to" + hour[h]            
    else:
        m = 60 - m 
        text = hour[m-1] + " minutes to " + hour[h]                
    return(text)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = int(input())
    m = int(input())
    result = timeInWords(h, m)
    fptr.write(result + '\n')
    fptr.close()

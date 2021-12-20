#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'preprocessDate' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY dates as parameter.
#

def preprocessDate(dates, n):
    
    months = {'Jan' : '01', 'Feb' : '02', 'Mar' : '03', 'Apr': '04', 'May' : '05', 'Jun': '06','Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    day = ''
    month = ''
    year = ''
    result = []
    
    for i in range(n) :
        
        date = dates[i].split()
        
        for index, item in enumerate(date) :

            if index == 0 :
                nday = re.findall('\d', item)
                
                if len(nday) == 1 :
                    day = '0' + ''.join(nday)
                
                else :
                    day = ''.join(nday)
                
            elif index == 1 :
                month = months[date[index]]
            
            elif index == 2 :
                year = date[2]
        ndate = year + '-' + month + '-' + day
        result.append(ndate)
    
    return result
                    

if __name__ == '__main__':

    dates_count = int(input().strip())

    dates = []

    for _ in range(dates_count):
        dates_item = input()
        dates.append(dates_item)

    result = preprocessDate(dates, dates_count)
    
    for i in range(dates_count) :
        print(result[i], sep =" ")
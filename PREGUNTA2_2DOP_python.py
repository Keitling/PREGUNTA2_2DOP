# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:21:36 2022

@author: Keitling Salinas

"""

from functools import reduce 

  
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], 
                                 range(n-2), [0, 1]) 
 
print(fib(10))


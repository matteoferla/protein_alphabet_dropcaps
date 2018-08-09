#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__description__ = \
    """

NB. Written for python 3, not tested under 2.
"""
__author__ = "Matteo Ferla. [Github](https://github.com/matteoferla)"
__email__ = "matteo.ferla@gmail.com"
__date__ = ""
__license__ = "Cite me!"
__version__ = "1.0"

from string import ascii_uppercase

css='''.drop-{L} {float: left;
                 font-size: .1px;
                 background: url('Alphabet_ray/{L}.png') no-repeat;
                 background-size: 40px;
                 padding: 40px 0 0 40px; 
                 margin-right: 9px;}
'''

for letter in ascii_uppercase:
    print(css.replace('{L}',letter))
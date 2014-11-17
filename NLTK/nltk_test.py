#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yang Sen C
# Date  : 2014-11-17 / Testing NLTK


import nltk
#from nltk.book import *


saying = ['After','all','is','said','and','done','more','is','said','than','done']

tokens = set(saying)
print tokens
tokens = sorted(tokens)
print tokens
print tokens[-2:]

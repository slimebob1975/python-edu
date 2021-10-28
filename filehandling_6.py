#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
try:
    f = open('./testfile.txt','r')
except:
    print("Filen kunde inte läsas!")
else:
    f.seek(0,2)
    print('Filesize: ', f.tell())

#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
with open('./testfile.txt','w') as f:
    rad = 'Filen testfile.txt'
    while rad:
        f.write(rad+'\n')
        rad = input('Skriv en rad (tom rad avslutar): ')
f.close()

with open('./testfile.txt','r') as f:
    for rad in f:
        print(rad, end='')
f.close()

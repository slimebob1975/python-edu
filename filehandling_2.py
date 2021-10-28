#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

try:
    f = open('./testfile.txt','w')
except:
    print("Filen kunde inte öppnas!")
else:
    rad = 'Filen testfile.txt'
    while rad:
        f.write(rad+'\n')
        rad = input('Skriv en rad (tom rad avslutar): ')
    f.close()

try:
    f = open('./testfile.txt','r')
except:
    print("Filen kunde inte läsas!")
else:
    for rad in f:
        print(rad, end='')
    f.close()

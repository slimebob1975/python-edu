#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
f = open('./testfile.txt','w')
rad = 'Filen testfile.txt'
while rad:
    f.write(rad+'\n')
    rad = input('Skriv en rad (tom rad avslutar): ')
f.close()

f = open('./testfile.txt','r')
for rad in f:
    print(rad, end='')
f.close()

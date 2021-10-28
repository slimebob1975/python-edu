#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

try:
    f = open('./testfile.txt','w')
except:
    print("Filen kunde inte öppnas!")
else:
    while True:
        namn = input('Skriv namn (return avslutar): ')
        if not namn:
            break
        adress = input('Skriv adress: ')
        telefon = input('Skriv telefon: ')
        f.write(namn+';'+adress+';'+telefon+'\n')
    f.close()

try:
    f = open('./testfile.txt','r')
except:
    print("Filen kunde inte läsas!")
else:
    i = 0
    for rad in f:
        i += 1
        post = rad.strip().split(';')
        print('Post '+str(i)+': ', post)
    f.close()
